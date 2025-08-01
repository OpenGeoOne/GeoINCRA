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
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterBoolean,
					   QgsExpressionContextUtils,
					   QgsExpressionContext,
					   QgsProcessingParameterFeatureSource,
					   QgsFeatureRequest,
					   QgsProcessingAlgorithm,
					   QgsProcessingParameterFileDestination)

from math import modf
from qgis.PyQt.QtGui import QIcon
from GeoINCRA.images.Imgs import *
import os


class createTemplate(QgsProcessingAlgorithm):

	VERTICE = 'VERTICE'
	LIMITE  = 'LIMITE'
	PARCELA  ='PARCELA'
	OUTPUT = 'OUTPUT'
	DEC_COORD = 'DEC_COORD'
	VER_Z = 'VER_Z'
	ABRIR = 'ABRIR'
	DEC_PREC = 'DEC_PREC'

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
                      <a href="https://geoone.com.br/pvgeoincra2/"><span style="font-weight: bold;">Conheça o curso de GeoINCRA no QGIS</span></a>
                      </p>
                      <p align="right">
                      <a href="https://portal.geoone.com.br/m/lessons/georreferenciamento-de-imveis-rurais-com-o-plugin-geoincra-1690158094835"><span style="font-weight: bold;">Acesse seu curso na GeoOne</span></a>
                      </p>
					  <a target="_blank" rel="noopener noreferrer" href="https://geoone.com.br/"><img height="80" title="GeoOne" src="data:image/png;base64,'''+ GeoOne +'''"></a>
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
            QgsProcessingParameterNumber(
                self.DEC_COORD,
                self.tr('Casas decimais das coordenadas'),
                type = QgsProcessingParameterNumber.Type.Integer,
                defaultValue = 3,
                minValue = 3
            )
        )

		self.addParameter(
            QgsProcessingParameterNumber(
                self.DEC_PREC,
                self.tr('Casas decimais das precisões e altitude'),
                type = QgsProcessingParameterNumber.Type.Integer,
                defaultValue = 2,
                minValue = 2
            )
        )

		self.addParameter(
            QgsProcessingParameterBoolean(
                self.VER_Z,
                self.tr('Verificar preenchimento de cota Z'),
                defaultValue = False
            )
        )

		self.addParameter(
			QgsProcessingParameterFileDestination(
				self.OUTPUT,
				self.tr('TXT de dados da Planilha ODS'),
				self.tr('Texto (*.txt)')
			)
		)

		self.addParameter(
            QgsProcessingParameterBoolean(
                self.ABRIR,
                self.tr('Abrir automaticamente'),
                defaultValue = True
            )
        )

	def vld_0(self, vertice, limite, parcela):
		if parcela is None or parcela.featureCount() != 1:
			raise QgsProcessingException('A camada Parcela deve conter exatamente uma feição selecionada!')
		if vertice is None or vertice.featureCount() == 0:
			raise QgsProcessingException('A camada Vértice não pode estar vazia!')
		if limite is None or limite.featureCount() == 0:
			raise QgsProcessingException('A camada Limite não pode estar vazia!')

	def vld_1(self, vertice):
		for feat in vertice.getFeatures():
			id_feat = feat.id()
			sigma_x = feat['sigma_x']
			sigma_y = feat['sigma_y']
			sigma_z = feat['sigma_z']
			metodo = feat['metodo_pos']
			tipo = feat['tipo_verti']
			vert = str(feat['vertice']).strip().upper()
			if not (0 <= sigma_x <= 10):
				raise QgsProcessingException(f'Erro no vértice {id_feat}: sigma_x fora do intervalo (0 a 10). Valor encontrado: {sigma_x}')
			if not (0 <= sigma_y <= 10):
				raise QgsProcessingException(f'Erro no vértice {id_feat}: sigma_y fora do intervalo (0 a 10). Valor encontrado: {sigma_y}')
			if not (0 <= sigma_z <= 10):
				raise QgsProcessingException(f'Erro no vértice {id_feat}: sigma_z fora do intervalo (0 a 10). Valor encontrado: {sigma_z}')
			if metodo not in ('PG1', 'PG2', 'PG3', 'PG4', 'PG5', 'PG6', 'PG7', 'PG8', 'PG9',
							'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'PT7', 'PT8', 'PT9',
							'PA1', 'PA2', 'PA3', 'PS1', 'PS2', 'PS3', 'PS4', 'PB1', 'PB2'):
				raise QgsProcessingException(f'Erro no vértice {id_feat}: método de posicionamento inválido: {metodo}')
			if tipo not in ('M', 'P', 'V'):
				raise QgsProcessingException(f'Erro no vértice {id_feat}: tipo de vértice inválido: {tipo}')
			if len(vert) < 7:
				raise QgsProcessingException(f'Erro no vértice {id_feat}: nome do vértice deve ter ao menos 7 caracteres. Valor encontrado: "{vert}"')
			if vert == 'NULL':
				raise QgsProcessingException(f'Erro no vértice {id_feat}: valor do código vértice está nulo ("NULL")')
		return True  # Validação bem-sucedida

	def vld_2(self,limite,vertice):
		pontos_vertice = {feat.geometry().asPoint() for feat in vertice.getFeatures()}
		for feat in limite.getFeatures():
			if feat['tipo'] not in ('LA1', 'LA2', 'LA3', 'LA4', 'LA5', 'LA6', 'LA7', 'LN1', 'LN2', 'LN3', 'LN4', 'LN5', 'LN6'):
				raise QgsProcessingException('Verifique os valores do atributo "tipo" na camada Limite!')
			if len(feat['confrontan']) < 3:
				raise QgsProcessingException('Verifique os valores do atributo "confrontante"!')
			for ponto in feat.geometry().asPolyline():
				if ponto not in pontos_vertice:
					raise QgsProcessingException('Ponto de coordenadas ({}, {}) da camada Limite não tem correspondente na camada Vértice!'.format(ponto.y(), ponto.x()))

	def vld_3(self,parcela,vertice):
		pontos_vertice = {feat.geometry().asPoint() for feat in vertice.getFeatures()}
		for feat in parcela.getFeatures():
			if feat.geometry().isMultipart():
				pols = feat.geometry().asMultiPolygon()
			else:
				pols = [feat.geometry().asPolygon()]
			for pol in pols:
				for ponto in pol[0]:
					if ponto not in pontos_vertice:
						raise QgsProcessingException('Ponto de coordenadas ({}, {}) da camada Parcela não tem correspondente na camada Vértice!'.format(ponto.y(), ponto.x()))

	def vld_z (self, vertice):
		for feat1 in vertice.getFeatures():
			z = float(feat1.geometry().constGet().z())
			if str(z) == 'nan' or z == 0:
				raise QgsProcessingException('Cota Z não preenchida ou igual a zero no ponto de coordenadas ({}, {})!'.format(pnt.y(), pnt.x()))

	def dd2dms(self, dd, n_digits=3):

		dd = abs(dd)
		frac, graus = modf(dd)
		frac, minutos = modf(frac * 60)
		segundos = round(frac * 60, n_digits)

		if segundos == 60:
			minutos += 1
			segundos = 0
		if minutos == 60:
			graus += 1
			minutos = 0

		return f"{int(graus):02d} {int(minutos):02d} {segundos:0{3+n_digits}.{n_digits}f}".replace('.', ',')


	def vertice (self,pnt,vertice,dec_coord,dec_prec):
		dec_prec = str(dec_prec)
		for feat in vertice.getFeatures():
			vert = feat.geometry().asPoint()
			if vert == pnt:
				codigo = feat['vertice'].strip()
				longitude = self.dd2dms(vert.x(), dec_coord) + ' W'
				sigma_x = ('{:.'+ dec_prec + 'f}').format(feat['sigma_x']).replace('.',',')
				latitude = self.dd2dms(vert.y(), dec_coord) + str(' S' if vert.y() < 0 else self.dd2dms(vert.y(), 3) + ' N')
				sigma_y = ('{:.'+ dec_prec + 'f}').format(feat['sigma_y']).replace('.',',')
				z = float(feat.geometry().constGet().z())
				if str(z) != 'nan':
					altitude = ('{:.'+ dec_prec + 'f}').format(z).replace('.',',')
				else:
					altitude = '0,00'
					feedback.reportError('Advertência: Ponto de código {} está com altitude igual a 0 (zero). Verifique!'.format(codigo))
				sigma_z = ('{:.'+ dec_prec + 'f}').format(feat['sigma_z']).replace('.',',')
				metodo_pos = feat['metodo_pos']
				return codigo,longitude,sigma_x,latitude,sigma_y,altitude, sigma_z,metodo_pos

	def limite (self,pnt,pnt_seg,limite):
		for feat in limite.getFeatures():
			linha = feat.geometry().asPolyline()
			for k2, vert in enumerate(linha[:-1]):
				if vert == pnt and linha[k2 + 1] == pnt_seg:
					tipo = feat['tipo']
					confrontan = feat['confrontan'].strip()
					cns = str(feat['cns']).replace('NULL', '').strip()
					matricula = str(feat['matricula']).replace('NULL', '').strip()
					return tipo,confrontan,cns,matricula
		raise QgsProcessingException(f'Erro de topologia: Limite não encontrado para ({pnt.y()}, {pnt.x()}) -> ({pnt_seg.y()}, {pnt_seg.x()})')

	def setInf(self, k, vertice, limite, arq, feat, dec_coord, dec_prec,prefix):
		pnt_str = []
		arq.write(prefix)
		for k1, pnt in enumerate(feat[:-1]):
			codigo, longitude, sigma_x, latitude, sigma_y, altitude, sigma_z, metodo_pos = self.vertice(pnt, vertice, dec_coord, dec_prec)
			pnt_seg = feat[k1 + 1]
			tipo, confrontan, cns, matricula = self.limite(pnt, pnt_seg, limite)

			arq.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(codigo, longitude, sigma_x, latitude, sigma_y, altitude, sigma_z, metodo_pos, tipo, cns.replace('\n',''), matricula.replace('\n','') , confrontan.replace('\n','')))

		return arq

	def reorder_polygon_points(self,pontos):
		ponto_inicial = None
		max_latitude = -90  # Latitude mínima possível
		for pnt in (pontos[:-1]):
			if pnt.y() > max_latitude:
				max_latitude = pnt.y()
				ponto_inicial = pnt

		index = pontos.index(ponto_inicial)
		pontos_reordenados = pontos[index:] + pontos[1:index+1]
		return(pontos_reordenados)

	def processAlgorithm(self, parameters, context, feedback):

		vertice = self.parameterAsSource(
			parameters,
			self.VERTICE,
			context
		)
		if vertice is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.VERTICE))

		limite = self.parameterAsSource(
			parameters,
			self.LIMITE,
			context
		)
		if limite is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.LIMITE))

		context.setInvalidGeometryCheck(QgsFeatureRequest.GeometryNoCheck)
		parcela = self.parameterAsSource(
			parameters,
			self.PARCELA,
			context
		)
		if parcela is None:
			raise QgsProcessingException(self.invalidSourceError(parameters, self.PARCELA))

		dec_coord = self.parameterAsInt(
			parameters,
			self.DEC_COORD,
			context
		)

		dec_prec = self.parameterAsInt(
			parameters,
			self.DEC_PREC,
			context
		)

		abrir = self.parameterAsBool(
		   parameters,
		   self.ABRIR,
		   context
		)

		ver_z = self.parameterAsBool(
		   parameters,
		   self.VER_Z,
		   context
		)


		output_path = self.parameterAsString(
			parameters,
			self.OUTPUT,
			context
		)
		if not output_path:
			raise QgsProcessingException('Caminho de saída inválido!')


		# Validações
		self.vld_0(vertice, limite, parcela)
		self.vld_1(vertice)
		self.vld_2(limite,vertice)
		self.vld_3(parcela,vertice)
		if ver_z:
			# Verificar altitude Z não preenchida
			self.vld_z (vertice)

		# Preencher cabeçalho
		arq =  open(output_path,'w')

		# map
		nat_ser = {1:'Particular', 2:'Contrato com Administração Pública'}
		pessoa  = {1:'Física', 2:'Jurídica'}
		situacao = {1:'Imóvel Registrado', 2:'Área Titulada não Registrada', 3:'Área não Titulada'}
		natureza = {1:'Assentamento',2:'Assentamento Parcela',3:'Estrada',4:'Ferrovia',5:'Floresta Pública',6:'Gleba Pública',7:'Particular',8:'Perímetro Urbano',9:'Terra Indígena',10:'Terreno de Marinha',11:'Terreno Marginal',12:'Território Quilombola',13:'Unidade de Conservação'}

		feature = next(parcela.getFeatures())

		arq.write('Natureza do Serviço: ' + (nat_ser[feature['nat_serv']] if feature['nat_serv'] in nat_ser else '')  + '\n')
		arq.write('Tipo Pessoa: ' + (pessoa[feature['pessoa']] if feature['pessoa'] in pessoa else '') + '\n')
		arq.write('Nome: ' + str(feature['nome']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('CPF: ' + str(feature['cpf_cnpj']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('Denominação: ' + str(feature['denominacao']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('Situação: ' + (situacao[feature['situacao']] if feature['situacao'] in situacao else '') + '\n')
		arq.write('Natureza da área: ' + (natureza[feature['natureza']] if feature['natureza'] in natureza else '') + '\n')
		arq.write('Código do Imóvel (SNCR/INCRA): ' + str(feature['sncr']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('Código do cartório (CNS): ' + str(feature['cod_cartorio']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('Matricula: ' + str(feature['matricula']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('Município: ' + str(feature['municipio']).replace('NULL', '').replace('\n','') + '\n')
		arq.write('UF: ' + str(feature['uf']).replace('\n',''))


		geom = feature.geometry()
		polygons = geom.asMultiPolygon() if geom.isMultipart() else [geom.asPolygon()]

		mapping = {0: []}
		for i, features in enumerate(polygons):
			mapping[0].append(self.reorder_polygon_points(features[0]))
			reorder = [self.reorder_polygon_points(feat) for feat in features[1:]]
			if reorder:
				mapping[i + 1] = reorder


		for n, feat in enumerate(mapping[0]):
			prefix = f'\n\nperimetro_1_{n+1}\nParcela número:{n+1:03d}\nLado: Externo\n\n'
			arq = self.setInf (n,vertice, limite, arq, feat, dec_coord, dec_prec, prefix)

		k=0
		for prm ,features in list(mapping.items())[1:]:
			for feat in features:
				k+=1
				prefix = f'\n\nperimetro_{prm+1}\nParcela número:{k:03d}\nLado: Interno (área encravada)\n\n'
				arq = self.setInf (k,vertice, limite, arq, feat, dec_coord, dec_prec, prefix)

		arq.close()

		if abrir:
			try:
				os.popen(output_path)
			except:
				feedback.pushInfo('Abra o arquivo de saída na pasta {}'.format(output_path))


		return {self.OUTPUT: output_path}
