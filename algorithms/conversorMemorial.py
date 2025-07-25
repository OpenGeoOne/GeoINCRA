# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeoINCRA
                                 A QGIS plugin
 Georreferenciamento de Imóveis Rurais
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-02-13
        copyright            : (C) 2022 by Tiago Prudencio e Leandro França
        email                : contato@geoone.com.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Tiago Prudencio e Leandro França'
__date__ = '2025-05-29'
__copyright__ = '(C) 2025 by Tiago Prudencio e Leandro França'

from qgis.PyQt.QtCore import QCoreApplication
from PyQt5.QtCore import *
from qgis.core import (QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterEnum,
                       QgsCoordinateReferenceSystem,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterNumber)
from qgis import processing
from qgis.PyQt.QtGui import QIcon
from GeoINCRA.images.Imgs import *
import os, re
from datetime import datetime
import platform

class ConversorMemorial(QgsProcessingAlgorithm):

    PDF = 'PDF'
    PERIMETRO = 'PERIMETRO'
    HTML = 'HTML'
    COORD = 'COORD'
    ANEL = 'ANEL'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ConversorMemorial()

    def name(self):
        return 'ConversorMemorial'.lower()

    def displayName(self):

        return self.tr('Conversor de Memorial do Sigef')

    def group(self):

        return self.tr(self.groupId())

    def groupId(self):

        return ''

    def icon(self):
        return QIcon(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images/geoincra_pb.png'))

    def shortHelpString(self):
        txt = '''Converte automaticamente o memorial descritivo tabular do SIGEF (PDF) em um texto narrativo mais fluido, mantendo os elementos técnicos exigidos, com formato adequado para leitura e uso em cartórios de registro de imóveis.
        Ideal para complementar o memorial tabular conforme exigências legais ou práticas cartorárias.'''
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
        QgsProcessingParameterFile(
            self.PDF,
            self.tr('Memorial Tabular do Sigef (PDF)'),
            fileFilter= 'Arquivo PDF (*.pdf)'
            )
        )

        opcoes = [self.tr('(lon,lat,h)'),
                  self.tr('(lat,lon,h)'),
                  self.tr('(lon,lat)'),
                  self.tr('(lat,lon)'),
                  '(lon,lat,h)' + self.tr(' com sufixo'),
                  '(lat,lon,h)' + self.tr(' com sufixo'),
                  '(lon,lat)' + self.tr(' com sufixo'),
                  '(lat,lon)' + self.tr(' com sufixo')
               ]

        self.addParameter(
            QgsProcessingParameterEnum(
                self.COORD,
                self.tr('Padrão de Coordenadas'),
				options = opcoes,
                defaultValue= 5
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.ANEL,
                self.tr('Anel'),
                type = QgsProcessingParameterNumber.Type.Integer,
                minValue = 1,
                optional = True
                )
            )

        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.HTML,
                self.tr('Memorial Descritivo Textual (HTML)'),
                self.tr('HTML files (*.html)')
            )
        )


    def processAlgorithm(self, parameters, context, feedback):

        pdf_path = self.parameterAsString(
            parameters,
            self.PDF,
            context
        )

        coordenadas = self.parameterAsEnum(
            parameters,
            self.COORD,
            context
        )

        anel = self.parameterAsInt(
            parameters,
            self.ANEL,
            context
        )

        if pdf_path is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.PDF))

        # Detectando o sistema operacional e instalando PyPDF2
        system_os = platform.system()
        if system_os == "Linux":
            import subprocess
            import sys
            try:
                from PyPDF2 import PdfReader
            except:
                feedback.pushInfo('PyPDF2 não está instalado. Tentando instalar "PyPDF2" utilizando "pip"...')
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"],
                                           stdout=subprocess.DEVNULL,
                                           stderr=subprocess.DEVNULL)
                    from PyPDF2 import PdfReader
                except subprocess.CalledProcessError as e:
                    feedback.reportError(f"Erro ao instalar o pacote pacote PyPDF2. Você pode tentar instalar manualmente via OSGeo4W Shell:\n"
                             f"python3 -m pip install PyPDF2")
                    raise QgsProcessingException(f"Falha ao instalar o pacote PyPDF2: {e}")
        else: # "Windows","Darwin" (MacOS)
            import pip
            try:
                from PyPDF2 import PdfReader
            except ImportError:
                feedback.pushInfo('PyPDF2 não está instalado. Tentando instalar "PyPDF2" utilizando "pip"...')
                try:
                    # Executa o pip usando subprocess
                    pip.main(["install","PyPDF2"])
                    from PyPDF2 import PdfReader
                except Exception as e:
                    feedback.reportError(f"Erro ao instalar o pacote pacote PyPDF2. Você pode tentar instalar manualmente via OSGeo4W Shell:\n"
                             f"pip install PyPDF2")
                    raise QgsProcessingException(f"Falha ao instalar o pacote PyPDF2: {e}")
        feedback.pushInfo('Biblioteca PyPDF2 importada com sucesso...')

        # Sistema de Referência de Coordenadas
        SRC = QgsCoordinateReferenceSystem('EPSG:4674')

        # Lendo arquivo PDF
        reader = PdfReader(pdf_path)
        text = ''
        # Iterar por cada página do PDF
        for page_num, page in enumerate(reader.pages):
            text += page.extract_text()

        dic = {
        'Denominação:': '',
        'Proprietário:': '',
        'Proprietário(a):': '',
        'Matrícula do imóvel:': '',
        'Transcrição do imóvel:': '',
        'Natureza da Área:': '',
        'CPF:': '',
        'CNJP:': '',
        'Município/UF:': '',
        'Código INCRA/SNCR:': '',
        'Responsável Técnico:': '',
        'Responsável Técnico(a):': '',
        'Formação:': '',
        'Conselho Profissional:': '',
        'Código de credenciamento:': '',
        'Documento de RT:': '',
        'Cartório (CNS):': '',
        'Área (Sistema Geodésico Local)': '',
        'Perímetro (m)': '',
        'Data Certificação': '',
        }

        chaves = list(dic.keys())

        lista_cod = []
        dic_cod = {}
        ind_encravado = []

        # Dividir o texto em linhas
        lines = text.splitlines()
        sentinela = False
        sentinela2 = False
        cont = 0
        pattern = r'\s*[A-Z0-9]{3,4}-[PMOV]-[A-Z0-9]{1,5}(?:,\s*[A-Z0-9]{3,4}-[PMOV]-[A-Z0-9]{1,5})*' #r'^\s*[A-Z0-9]{3,4}-[MPV]-\d{1,5}$'

        for line in lines:

            if sentinela:
                dic[item] = line
                sentinela = False

            for item in dic:
                if item in line:
                    sentinela = True
                    break

            if cont == 8:
                cont = 0
                sentinela2 = False

            if bool(re.fullmatch(pattern, line)):
                if cont == 0:
                    codigo = line.strip()
                    lista_cod.append(codigo)
                    sentinela2 = True

            if 'Área encravada' in line:
                ind_encravado.append(len(lista_cod))

            elif sentinela2:
                cont += 1
                if cont == 1:
                    dic_cod[lista_cod[-1]] = {'lon':'', 'lat':'', 'h':'', 'cns':'', 'matr':'', 'confr': '', 'az': '', 'dist': '', 'texto_confr': ''}
                if cont == 2:
                    dic_cod[lista_cod[-1]]['lon'] = line.strip()
                if cont == 3:
                    dic_cod[lista_cod[-1]]['lat'] = line.strip()
                if cont == 4:
                    dic_cod[lista_cod[-1]]['h'] = line.strip()
                if cont == 6:
                    dic_cod[lista_cod[-1]]['az'] = line.strip()
                if cont == 7:
                    dic_cod[lista_cod[-1]]['dist'] = line.strip()
                if cont == 8:
                    try:
                        cns,mat,confr = line.strip().split('|')
                        cns = cns.split(':')[-1].strip()
                        matr = mat.strip().split()[-1]
                        confr = confr.strip()
                        dic_cod[lista_cod[-1]]['cns'] = cns
                        dic_cod[lista_cod[-1]]['matr'] = matr
                        dic_cod[lista_cod[-1]]['confr'] = confr
                        dic_cod[lista_cod[-1]]['texto_confr'] = line
                    except:
                        dic_cod[lista_cod[-1]]['confr'] = line.strip()


        if len(lista_cod) == 0 or dic['Denominação:'] == '':
            raise QgsProcessingException('PDF de entrada não é um Memorial do Sigef!')

        feedback.pushInfo('Alimentando arquivo HTML...')

        # Se encravado, fatiar lista_cod
        def fatiar_lista(a, ind):
            ind = [0] + ind + [len(a)]
            return [a[ind[i]:ind[i+1]] for i in range(len(ind)-1)]

        if len(ind_encravado) > 0:
            listas_fat = fatiar_lista(lista_cod, ind_encravado)
        else:
            listas_fat = [lista_cod]


        # Escolher anel
        if anel:
            if anel <= len(listas_fat):
                ind = anel-1
            else:
                raise QgsProcessingException('Valor inválido para o número do anel!')
        else:
            ind = 0
        lista_cod_fat = listas_fat[ind]


        # Modelo de coordenadas
        def CoordN (x, y, z):
            if coordenadas > 3: # com sufixo
                x = x[1:]+'W'
                y = y[1:]+'S' if y[0] == '-' else y[1:]+'N'
            if coordenadas == 0:
                txt = '''<b>longitude [Xn]</b>, <b>latitude [Yn]</b> e <b>h [Zn]m</b>'''
            elif coordenadas == 1:
                txt = '''<b>latitude [Yn]</b>, <b>longitude [Xn]</b> e <b>h [Zn]m</b>'''
            elif coordenadas == 2:
                txt = '''<b>longitude [Xn]</b> e <b>latitude [Yn]</b>'''
            elif coordenadas == 3:
                txt = '''<b>latitude [Yn]</b> e <b>longitude [Xn]</b>'''
            elif coordenadas == 4:
                txt = '''<b>[Xn]</b>, <b>[Yn]</b> e <b>h [Zn]m</b>'''
            elif coordenadas == 5:
                txt = '''<b>[Yn]</b>, <b>[Xn]</b> e <b>h [Zn]m</b>'''
            elif coordenadas == 6:
                txt = '''<b>[Xn]</b> e <b>[Yn]</b>'''
            elif coordenadas == 7:
                txt = '''<b>[Yn]</b> e <b>[Xn]</b>'''
            return txt.replace('[Yn]', self.str2HTML(y)).replace('[Xn]', self.str2HTML(x)).replace('[Zn]', self.str2HTML(z))

        LOGO = 'png;base64,'+ GeoOne
        SLOGAN = 'Mapeamento automatizado, fácil e direto ao ponto é na GeoOne!'

        texto_inicial = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
      <meta content="text/html; charset=ISO-8859-1"
     http-equiv="content-type">
      <title>'''+ self.str2HTML('Memorial descritivo') + '''</title>
      <link rel = "icon" href = "https://github.com/OpenGeoOne/GeoINCRA/blob/main/images/geoincra.png?raw=true" type = "image/x-icon">
    </head>
    <body>
    <div style="text-align: center;"><span style="font-weight: bold;"><br>
    <a target="_blank" rel="noopener noreferrer" href="https://geoone.com.br/"><img height="80" src="data:image/'''+ LOGO + '''"></a>
    <br><i>'''+ self.str2HTML(SLOGAN) + '''</i></span><br style="font-weight: bold;">
    <br></div>
    <p class="western"
     style="margin-bottom: 0.0001pt; text-align: center;"
     align="center"><b><u><span style="font-size: 12pt;">'''+ self.str2HTML(self.tr('MEMORIAL DESCRITIVO')) + '''</span></u></b></p>
    <p class="western" style="margin-bottom: 0.0001pt;"><o:p>&nbsp;</o:p></p>
    <table class="MsoTableGrid"
     style="border: medium none ; border-collapse: collapse;"
     border="0" cellpadding="0" cellspacing="0">
      <tbody>
        <tr style="">
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>'''+ self.str2HTML(self.tr('Imóvel')) + ''': </b>[IMOVEL]</p>
          </td>
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Código INCRA/SNCR')) + ''':</b>
    [REGISTRO]</p>
          </td>
        </tr>
        <tr style="">
          <td colspan="2"
     style="padding: 0cm 5.4pt;" valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Proprietário(a)')) + ''': </b>[PROPRIETARIO]</p>
          </td>
        </tr>
        <tr style="">
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Município')) + ''':</b>
    [MUNICIPIO]<b></b></p>
          </td>
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Estado')) + ''':
          </b>[UF]</p>
          </td>
        </tr>
        <tr style="">
          <td colspan="2"
     style="padding: 0cm 5.4pt;" valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Matrícula/Transcrição')) + ''':</b>
    [MATRICULAS]</p>
          </td>
        </tr>
        <tr style="">
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Área (ha)')) + ''': </b>[AREA]</p>
          </td>
          <td style="padding: 0cm 5.4pt;"
     valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Perímetro')) + ''' (m):</b> [PERIMETRO]</p>
          </td>
        </tr>
        <tr style="">
          <td colspan="2"
     style="padding: 0cm 5.4pt;" valign="top">
          <p class="western" style="margin-bottom: 0.0001pt;"><b>''' + self.str2HTML(self.tr('Sistema de Referência de Coordenadas')) + ''':</b> [SRC]<b></b></p>
          </td>
        </tr>
      </tbody>
    </table>
    <p class="western" style="margin-bottom: 0.0001pt;"><o:p>&nbsp;</o:p></p>
    <p class="western"
     style="margin-bottom: 0.0001pt; text-align: justify;">'''+ self.str2HTML(self.tr('Inicia-se a descrição deste perímetro n'))

        texto_var1 = self.str2HTML(self.tr('o vértice ')) + '''<b>[Vn]</b>, '''+ self.str2HTML(self.tr('de coordenadas ')) + '''[Coordn],
    '''+ self.str2HTML(self.tr('deste, segue confrontando com [Confront_k], com os seguintes azimutes e distâncias: [Az_n] e [Dist_n]m até '))

        texto_var2 = self.str2HTML(self.tr('o vértice ')) + '''<span> </span><b>[Vn]</b>, ''' + self.str2HTML(self.tr('de coordenadas ')) + '''[Coordn]; '''+ self.str2HTML(self.tr('[Az_n] e [Dist_n]m até '))

        # Coordenadas Geo, cálculo em SGL e Azimute Puissant:
        texto_calculo = self.tr('. Os azimutes foram calculados pela fórmula do Problema Geodésico Inverso segundo Puissant. As distâncias, área e perímetro foram calculados no Sistema Geodésico Local (SGL) com origem na média das coordenadas cartesianas geocêntricas do imóvel.')

        texto_final = self.str2HTML(self.tr('o vértice ')) + '''<b>[P-01]</b>, '''+ self.tr('de coordenadas') + ''' [Coord1],
    ''' + self.str2HTML(self.tr('ponto inicial da descrição deste perímetro. Todas as coordenadas aqui descritas estão georreferenciadas ao Sistema Geodésico de Referência (SGR)')) + ''' <b>[GRS]</b>''' + self.str2HTML(texto_calculo) + '''
     </p>
    <p class="western"
     style="margin-bottom: 0.0001pt; text-align: right;"
     align="right">[LOCAL], [DATA].</p>

     <p class="western" style="margin-bottom: 0.0001pt;"><o:p>&nbsp;</o:p></p>
     <p class="western"
      style="margin: 0cm 0cm 0.0001pt; text-align: center;"
      align="center">___________________________________________</p>
     <p class="western"
      style="margin: 0cm 0cm 0.0001pt; text-align: center;"
      align="center">[OWNER]</p>
     <p class="western"
      style="margin: 0cm 0cm 0.0001pt; text-align: center;"
      align="center">''' + self.str2HTML(self.tr('PROPRIETÁRIO DO IMÓVEL')) + '''</p>

    <p class="western" style="margin-bottom: 0.0001pt;"><o:p>&nbsp;</o:p></p>
    <p class="western"
     style="margin: 0cm 0cm 0.0001pt; text-align: center;"
     align="center">___________________________________________</p>
    <p class="western"
     style="margin: 0cm 0cm 0.0001pt; text-align: center;"
     align="center">[RESP_TEC]</p>
    <p class="western"
     style="margin: 0cm 0cm 0.0001pt; text-align: center;"
     align="center">[CREA]</p>
    <p class="western"
     style="margin: 0cm 0cm 0.0001pt; text-align: center;"
     align="center">''' + self.str2HTML(self.tr('RESPONSÁVEL TÉCNICO')) + '''</p>
    <p class="MsoNormal"><o:p>&nbsp;</o:p></p>
    </body>
    </html>
    '''
        # Inserindo dados iniciais do levantamento
        proprietario = dic['Proprietário(a):'] if dic['Proprietário(a):'] else dic['Proprietário:']
        matricula = dic['Matrícula do imóvel:'] if dic['Matrícula do imóvel:'] else dic['Transcrição do imóvel:']
        itens = {'[IMOVEL]': self.str2HTML(dic['Denominação:']),
                '[PROPRIETARIO]': self.str2HTML(proprietario),
                '[MATRICULAS]': self.str2HTML(str(matricula) + ' | CNS: ' + dic['Cartório (CNS):']),
                '[AREA]': self.str2HTML(dic['Área (Sistema Geodésico Local)']),
                '[SRC]': self.str2HTML('SIRGAS2000'),
                '[REGISTRO]': self.str2HTML(dic['Código INCRA/SNCR:']),
                '[MUNICIPIO]': self.str2HTML(dic['Município/UF:'].split('-')[0]),
                '[UF]': self.str2HTML(dic['Município/UF:'].split('-')[-1]),
                '[PERIMETRO]': self.str2HTML(dic['Perímetro (m)']),
                    }

        for item in itens:
                texto_inicial = texto_inicial.replace(item, itens[item])

        LINHAS = texto_inicial
        mudou = True
        for k,codigo in enumerate(lista_cod_fat):
            if mudou:
                linha0 = texto_var1
                itens =    {'[Vn]': self.str2HTML(codigo),
                            '[Coordn]': CoordN(dic_cod[codigo]['lon'], dic_cod[codigo]['lat'], dic_cod[codigo]['h']),
                            '[Az_n]': self.str2HTML(dic_cod[codigo]['az']),
                            '[Dist_n]': self.str2HTML(dic_cod[codigo]['dist']),
                            '[Confront_k]': self.str2HTML(dic_cod[codigo]['confr'])
                            }
                for item in itens:
                    linha0 = linha0.replace(item, itens[item])
                LINHAS += linha0
                #LIN0 = ''
                if dic_cod[codigo]['texto_confr']  == dic_cod[lista_cod_fat[0 if k+1 == len(lista_cod_fat) else k+1]]['texto_confr']:
                    mudou = False
            else:
                linha1 = texto_var2
                itens = {'[Vn]': self.str2HTML(codigo),
                        '[Coordn]': CoordN(dic_cod[codigo]['lon'], dic_cod[codigo]['lat'], dic_cod[codigo]['h']),
                        '[Az_n]': self.str2HTML(dic_cod[codigo]['az']),
                        '[Dist_n]': self.str2HTML(dic_cod[codigo]['dist'])
                        }
                for item in itens:
                    linha1 = linha1.replace(item, itens[item])
                LINHAS += linha1
                #LIN0 += linha1
                if dic_cod[codigo]['texto_confr']  != dic_cod[lista_cod_fat[0 if k+1 == len(lista_cod_fat) else k+1]]['texto_confr']:
                    mudou = True


        # Data do documento
        meses = {1: 'janeiro', 2:'fevereiro', 3: 'março', 4:'abril', 5:'maio', 6:'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
        try:
            dataAss = datetime.strptime(dic['Data Certificação'], '%d/%m/%Y %H:%M')
        except:
            try:
                dataAss = datetime.strptime(dic['Data Certificação'], '%d/%m/%y %H:%M')
            except:
                dataAss = None
        if dataAss:
            data_formatada = f"{dataAss.day:02d} de {meses[dataAss.month]} de {dataAss.year}"
        else:
            data_formatada = ''

        # Inserindo dados finais
        codigo = lista_cod_fat[0]
        itens = {   '[P-01]': self.str2HTML(codigo),
                    '[Coord1]': CoordN(dic_cod[codigo]['lon'], dic_cod[codigo]['lat'], dic_cod[codigo]['h']),
                    '[GRS]': 'SIRGAS 2000',
                    '[OWNER]': self.str2HTML(proprietario),
                    '[RESP_TEC]': self.str2HTML(dic['Responsável Técnico(a):'] if dic['Responsável Técnico(a):'] else dic['Responsável Técnico:']),
                    '[CREA]': self.str2HTML(dic['Formação:'] + ' | ' + dic['Conselho Profissional:']  + ' | ' + dic['Documento de RT:']),
                    '[LOCAL]': self.str2HTML(dic['Município/UF:']),
                    '[DATA]': self.str2HTML(data_formatada)
                    }

        for item in itens:
                texto_final = texto_final.replace(item, itens[item])
        LINHAS += texto_final
        output = self.parameterAsFileOutput(parameters, self.HTML, context)
        arq = open(output, 'w')
        arq.write(LINHAS)
        arq.close()

        return {self.HTML: output}


    def str2HTML(self, texto):
        if texto:
            dicHTML = {'Á': '&Aacute;',	'á': '&aacute;',	'Â': '&Acirc;',	'â': '&acirc;',	'À': '&Agrave;',	'à': '&agrave;',	'Å': '&Aring;',	'å': '&aring;',	'Ã': '&Atilde;',	'ã': '&atilde;',	'Ä': '&Auml;',	'ä': '&auml;', 'ú': '&uacute;', 'Ú': '&Uacute;', 'Æ': '&AElig;',	'æ': '&aelig;',	'É': '&Eacute;',	'é': '&eacute;',	'Ê': '&Ecirc;',	'ê': '&ecirc;',	'È': '&Egrave;',	'è': '&egrave;',	'Ë': '&Euml;',	'ë': '&Euml;',	'Ð': '&ETH;',	'ð': '&eth;',	'Í': '&Iacute;',	'í': '&iacute;',	'Î': '&Icirc;',	'î': '&icirc;',	'Ì': '&Igrave;',	'ì': '&igrave;',	'Ï': '&Iuml;',	'ï': '&iuml;',	'Ó': '&Oacute;',	'ó': '&oacute;',	'Ô': '&Ocirc;',	'ô': '&ocirc;',	'Ò': '&Ograve;', 'Õ': '&Otilde;', 'õ': '&otilde;',	'ò': '&ograve;',	'Ø': '&Oslash;',	'ø': '&oslash;',	'Ù': '&Ugrave;',	'ù': '&ugrave;',	'Ü': '&Uuml;',	'ü': '&uuml;',	'Ç': '&Ccedil;',	'ç': '&ccedil;',	'Ñ': '&Ntilde;',	'ñ': '&ntilde;',	'Ý': '&Yacute;',	'ý': '&yacute;',	'"': '&quot;', '”': '&quot;',	'<': '&lt;',	'>': '&gt;',	'®': '&reg;',	'©': '&copy;',	'\'': '&apos;', 'ª': '&ordf;', 'º': '&ordm;', '°':'&deg;', '²':'&sup2;', '¿':'&iquest;', '¡':'&iexcl;'}
            for item in dicHTML:
                if item in texto:
                    texto = texto.replace(item, dicHTML[item])
            return texto
        else:
            return ''
