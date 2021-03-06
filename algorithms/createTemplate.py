# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeoINCRA
								 A QGIS plugin
 Georreferenciamento de Imóveis Rurais
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
							  -------------------
		begin				: 2022-02-13
		copyright			: (C) 2022 by Tiago Prudencio e Leandro França
		email				: contato@geoone.com.br
 ***************************************************************************/

/***************************************************************************
 *																		 *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or	 *
 *   (at your option) any later version.								   *
 *																		 *
 ***************************************************************************/
"""

__author__ = 'Tiago Prudencio e Leandro França'
__date__ = '2022-02-13'
__copyright__ = '(C) 2022 by Tiago Prudencio e Leandro França'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
					   QgsProcessingException,
					   QgsGeometry,
					   QgsExpression,
					   QgsExpressionContextUtils,
					   QgsExpressionContext,
					   QgsProcessingParameterFeatureSource,
					   QgsProcessingAlgorithm,
					   QgsProcessingParameterFileDestination)

from math import floor
from qgis.PyQt.QtGui import QIcon
from GeoINCRA.images.Imgs import *
import os


class createTemplate(QgsProcessingAlgorithm):

	VERTICE = 'VERTICE'
	LIMITE  = 'LIMITE'
	PARCELA  ='PARCELA'
	OUTPUT = 'OUTPUT'

	def tr(self, string):
		return QCoreApplication.translate('Processing', string)

	def createInstance(self):
		return createTemplate()

	def name(self):
		return 'createtemplate'

	def displayName(self):
		return self.tr('Gerar TXT para Planilha ODS')

	def group(self):
		return self.tr(self.groupId())

	def groupId(self):
		return ''

	def icon(self):
		return QIcon(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images/geoincra_pb.png'))

	def shortHelpString(self):
		txt = "Cria um arquivo de Texto (TXT) com todas os dados necessários para preencher a planilha ODS do SIGEF."

		footer = '''<div>
					  <div align="center">
					  <img style="width: 100%; height: auto;" src="data:image/jpg;base64,'''+ INCRA_GeoOne +'''
					  </div>
					  <div align="right">
					  <p align="right">
					  <a href="https://github.com/OpenGeoOne/GeoINCRA/wiki/Sobre-o-GeoINCRA#banco-de-dados-georural"><span style="font-weight: bold;">Clique aqui para conhecer o modelo GeoRural da GeoOne</span></a><br>
					  </p>
					  <a target="_blank" rel="noopener noreferrer" href="https://geoone.com.br/"><img title="GeoOne" src="data:image/png;base64,'''+ GeoOne +'''"></a>
					  <p><i>"Mapeamento automatizado, fácil e direto ao ponto é na GeoOne!"</i></p>
					  </div>
					</div>'''
		return txt + footer

	def initAlgorithm(self, config=None):

		self.addParameter(
			QgsProcessingParameterFeatureSource(
				self.VERTICE,
				self.tr('Camada Vertice'),
				[QgsProcessing.TypeVectorPoint]
			)
		)

		self.addParameter(
			QgsProcessingParameterFeatureSource(
				self.LIMITE,
				self.tr('Camada Limite'),
				[QgsProcessing.TypeVectorLine]
			)
		)

		self.addParameter(
			QgsProcessingParameterFeatureSource(
				self.PARCELA,
				self.tr('Camada Parcela'),
				[QgsProcessing.TypeVectorPolygon]
			)
		)

		self.addParameter(
			QgsProcessingParameterFileDestination(
				self.OUTPUT,
				self.tr('TXT de dados da Planilha ODS'),
				self.tr('Texto (*.txt)')
			)
		)

	def processAlgorithm(self, parameters, context, feedback):

		vertice = self.parameterAsVectorLayer(
			parameters,
			self.VERTICE,
			context
		)
		if vertice is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.VERTICE))

		limite = self.parameterAsVectorLayer(
			parameters,
			self.LIMITE,
			context
		)
		if limite is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.LIMITE))

		parcela = self.parameterAsVectorLayer(
			parameters,
			self.PARCELA,
			context
		)
		if parcela is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.PARCELA))

		output_path = self.parameterAsString(
			parameters,
			self.OUTPUT,
			context
		)
		if not output_path:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.OUTPUT))

		# Validações

		# Checar preenchimento dos atributos da camada vértice
		for feat in vertice.getFeatures():
			if feat['sigma_x'] < 0 or feat['sigma_x'] > 10 or feat['sigma_x'] == None:
				raise QgsProcessingException ('Verifique os valores do atrituto "sigma_x"!')
			if feat['sigma_y'] < 0 or feat['sigma_y'] > 10 or feat['sigma_y'] == None:
				raise QgsProcessingException ('Verifique os valores do atrituto "sigma_y"!')
			if feat['sigma_z'] < 0 or feat['sigma_z'] > 10 or feat['sigma_z'] == None:
				raise QgsProcessingException ('Verifique os valores do atrituto "sigma_z"!')
			if feat['metodo_pos'] not in ('PG1', 'PG2', 'PG3', 'PG4', 'PG5', 'PG6', 'PG7', 'PG8', 'PG9', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'PT7', 'PT8', 'PA1', 'PA2', 'PS1', 'PS2', 'PS3', 'PS4'):
				raise QgsProcessingException ('Verifique os valores do atrituto "metodo_pos"!')
			if feat['tipo_verti'] not in ('M', 'P', 'V'):
				raise QgsProcessingException ('Verifique os valores do atrituto "tipo_vertice"!')
			if len(feat['vertice']) < 7:
				raise QgsProcessingException ('Verifique os valores do atrituto "código do vértice"!')


		# Camada parcela deve ter apenas uma feição selecionada
		if parcela.featureCount() != 1:
			raise QgsProcessingException ('Camada parcela deve ter apenas uma feição selecionada!')

		# Verificar se cada vértice da camada limite (linha) tem o correspondente da camada vétice (ponto)
		for feat1 in limite.getFeatures():
			# Checar preenchimento dos atributos
			if feat1['tipo'] not in ('LA1', 'LA2', 'LA3', 'LA4', 'LA5', 'LA6', 'LA7', 'LN1', 'LN2', 'LN3', 'LN4', 'LN5', 'LN6'):
				raise QgsProcessingException ('Verifique os valores do atributo "tipo"!')
			if len(feat1['confrontan']) < 3:
				raise QgsProcessingException ('Verifique os valores do atrituto "confrontante"!')
			# Topologia
			linha = feat1.geometry().asPolyline()
			for pnt in linha:
				corresp = False
				for feat2 in vertice.getFeatures():
					vert = feat2.geometry().asPoint()
					if vert == pnt:
						corresp = True
						continue
				if not corresp:
					raise QgsProcessingException('Ponto de coordenadas ({}, {}) da camada limite não possui correspondente na camada vértice!'.format(pnt.x(), pnt.y()))

		# Verificar se cada vértice da camada parcela (polígono) tem o correspondente da camada vétice (ponto)
		for feat1 in parcela.getFeatures():
			geom1 = feat1.geometry()
			if geom1.isMultipart():
				pols = geom1.asMultiPolygon()
			else:
				pols = [geom1.asPolygon()]
			for pol in pols:
				for pnt in pol[0]:
					corresp = False
					for feat2 in vertice.getFeatures():
						vert = feat2.geometry().asPoint()
						if vert == pnt:
							corresp = True
							continue
					if not corresp:
						raise QgsProcessingException('Ponto de coordenadas ({}, {}) da camada parcela não possui correspondente na camada vértice!'.format(pnt.x(), pnt.y()))

		# Outras validações - nós duplicados, feições duplicadas, relação entre atributos, altitude não preenchida ou igual a zero

		def dd2dms(dd, n_digits=3):
			if dd != 0:
				graus = int(floor(abs(dd)))
				resto = round(abs(dd) - graus, 10)
				minutos = int(floor(60*resto))
				resto = round(resto*60 - minutos, 10)
				segundos = resto*60
				if round(segundos,n_digits) == 60:
					minutos += 1
					segundos = 0
				if minutos == 60:
					graus += 1
					minutos = 0
				if dd < 0:
					texto = '{:02d}'.format(graus) + ' '
				else:
					texto = '{:02d}'.format(graus) + ' '
				texto = texto + '{:02d}'.format(minutos) + " "
				if n_digits < 1:
					texto = texto + '{:02d}'.format(int(segundos)) + ' '
				else:
					texto = texto + ('{:0' + str(3+n_digits) + '.' + str(n_digits) + 'f}').format(segundos) + ' '
				return texto.replace('.',',')
			else:
				texto = "00 00 " + ('{:0' + str(3+n_digits) + '.' + str(n_digits) + 'f}').format(0)
				return texto.replace('.',',')

		# Preencher cabeçalho
		arq =  open(output_path,'w')

		nat_ser = {1:'Particular', 2:'Contrato com Adm Pública'}
		pessoa, situacao  = {1:'Física', 2:'Jurídica'}, {1:'Imóvel Registrado', 2:'Área Titulada não Registrada', 3:'Área não Titulada'}

		arq.write('Natureza do Serviço: '+ nat_ser[feat1['nat_serv']]+ '\n')
		arq.write('Tipo Pessoa: '+ pessoa[feat1['pessoa']]+ '\n')
		arq.write('nome: '+ str(feat1['nome'])+ '\n')
		arq.write('CPF: '+ str(feat1['cpf_cnpj'])+ '\n')
		arq.write('Denominação: '+ str(feat1['denominacao'])+ '\n')
		arq.write('Situação: '+ situacao[feat1['situacao']]+ '\n')
		arq.write('Código do Imóvel (SNCR/INCRA): '+ str(feat1['sncr'])+ '\n')
		arq.write('Código do cartório (CNS): '+ str(feat1['cod_cartorio'])+ '\n')
		arq.write('Matricula: '+ str(feat1['matricula'])+ '\n')
		arq.write('Município: '+ str(feat1['municipio'])+ '\n')
		arq.write('UF: '+ str(feat1['uf'])+ '\n')

		# Preenchimento das Parcelas
		cont_parc = 0
		for feat1 in parcela.getFeatures():
			geom1 = feat1.geometry()
			if geom1.isMultipart():
				pols = geom1.asMultiPolygon()
			else:
				pols = [geom1.asPolygon()]
			for pol in pols:
				cont_parc += 1
				arq.write('\n\nParcela {}\n'.format(cont_parc))
				for pnt in pol[0][:-1]:
					for feat2 in vertice.getFeatures():
						vert = feat2.geometry().asPoint()
						if vert == pnt:
							codigo = feat2['vertice']
							longitude = dd2dms(vert.x(), 3) + 'W'
							sigma_x = '{:.2f}'.format(feat2['sigma_x']).replace('.',',')
							latitude = dd2dms(vert.y(), 3) + 'S' if vert.y() < 0 else dd2dms(vert.y(), 3) + 'N'
							sigma_y = '{:.2f}'.format(feat2['sigma_y']).replace('.',',')
							z = float(feat2.geometry().constGet().z())
							if str(z) != 'nan':
								altitude = '{:.2f}'.format(z).replace('.',',')
							else:
								altitude = '0,00'
								feedback.pushInfo('Advertência: Ponto de código {} está com altitude igual a 0 (zero). Verifique!'.format(codigo))
							sigma_z = '{:.2f}'.format(feat2['sigma_z']).replace('.',',')
							metodo_pos = feat2['metodo_pos']
							break
					for feat3 in limite.getFeatures():
						linha = feat3.geometry().asPolyline()
						sentinela = False
						for vert in linha[:-1]:
							if vert == pnt:
								tipo = feat3['tipo']
								confrontan = feat3['confrontan']
								cns = str(feat3['cns']).replace('NULL', '')
								matricula = str(feat3['matricula']).replace('NULL', '')
								sentinela = True
								break
						if sentinela:
							break
					arq.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(codigo, longitude, sigma_x, latitude, sigma_y, altitude, sigma_z, metodo_pos, tipo, cns, matricula , confrontan))

		arq.close()

		return {}
