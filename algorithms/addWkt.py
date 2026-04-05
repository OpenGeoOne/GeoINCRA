# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeoINCRA
                                 A QGIS plugin
 Georreferenciamento de Imóveis Rurais
 ***************************************************************************/
"""

__author__ = 'Tiago Prudencio e Leandro França'
__date__ = '2022-02-13'
__copyright__ = '(C) 2022 by Tiago Prudencio e Leandro França'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon

from qgis.core import (
    QgsFeature,
    QgsFeatureSink,
    QgsGeometry,
    QgsPoint,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterFile,
    QgsVectorLayer,
    QgsWkbTypes
)

from GeoINCRA.images.Imgs import *
import os
import csv


class addWkt(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return addWkt()

    def name(self):
        return 'addWkt'

    def displayName(self):
        return self.tr('CSV do INCRA para camada PointZ')

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return ''

    def icon(self):
        return QIcon(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'images/geoincra_pb.png'
            )
        )

    def tags(self):
        return 'GeoOne,GeoRural,INCRA,Sigef,CSV,vértice,vertice,PointZ,WKT'.split(',')

    def shortHelpString(self):
        txt = (
            'Esta ferramenta transforma um arquivo CSV com geometria WKT '
            'em uma camada do tipo PointZ. '
            'O arquivo deve conter geometria POINT em WKT e um campo Z.'
        )

        footer = '''<div>
                      <div align="center">
                      <img style="width: 100%; height: auto;" src="data:image/jpg;base64,''' + INCRA_GeoOne + '''">
                      </div>
                      <div align="right">
                      <p align="right">
                      <a href="https://geoone.com.br/pvgeoincra2/"><span style="font-weight: bold;">Conheça o curso de GeoINCRA no QGIS</span></a>
                      </p>
                      <p align="right">
                      <a href="https://portal.geoone.com.br/m/lessons/geoincra?classId=2232"><span style="font-weight: bold;">Acesse seu curso na GeoOne</span></a>
                      </p>
                      <a target="_blank" rel="noopener noreferrer" href="https://geoone.com.br/"><img height="80" title="GeoOne" src="data:image/png;base64,''' + GeoOne + '''"></a>
                      <p><i>"Mapeamento automatizado, fácil e direto ao ponto é na GeoOne!"</i></p>
                      </div>
                    </div>'''
        return txt + footer

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                self.INPUT,
                self.tr('Arquivo de entrada (*.csv)'),
                fileFilter='Arquivo de Valores Separados (*.csv)'
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Vértices do INCRA')
            )
        )

    # ---------------------------------------------------------------------
    # Utilitários
    # ---------------------------------------------------------------------

    def _read_header(self, file_path):
        """
        Lê o cabeçalho bruto do CSV e tenta detectar delimitador.
        Retorna (header_limpo, delimitador).
        """
        encodings = ['utf-8-sig', 'utf-8', 'latin1']

        last_error = None
        for enc in encodings:
            try:
                with open(file_path, 'r', encoding=enc, newline='') as f:
                    first_line = f.readline()
                    if not first_line:
                        raise QgsProcessingException(
                            self.tr('O arquivo CSV está vazio.')
                        )

                    # Detecta delimitador de forma simples e robusta
                    candidates = [';', ',', '\t', '|']
                    delimiter = max(candidates, key=lambda d: first_line.count(d))

                    f.seek(0)
                    reader = csv.reader(f, delimiter=delimiter)
                    header = next(reader)

                    # remove espaços e colunas vazias criadas por delimitador final
                    clean_header = [str(col).strip() for col in header if str(col).strip() != '']

                    return clean_header, delimiter

            except Exception as e:
                last_error = e

        raise QgsProcessingException(
            self.tr('Não foi possível ler o cabeçalho do CSV: {}').format(str(last_error))
        )

    def _find_field_name(self, header, candidates, case_sensitive=False):
        """
        Procura um nome de campo entre candidatos.
        """
        if case_sensitive:
            for name in candidates:
                if name in header:
                    return name
            return None

        header_map = {h.upper(): h for h in header}
        for name in candidates:
            if name.upper() in header_map:
                return header_map[name.upper()]
        return None

    def _parse_z_value(self, value):
        if value is None:
            raise ValueError('valor nulo')

        text = str(value).strip()
        if text == '':
            raise ValueError('valor vazio')

        text = text.replace(',', '.')
        return float(text)

    def _display_geom(self, wkb_type):
        return QgsWkbTypes.displayString(wkb_type)

    # ---------------------------------------------------------------------
    # Processamento
    # ---------------------------------------------------------------------

    def processAlgorithm(self, parameters, context, feedback):

        input_csv = self.parameterAsString(parameters, self.INPUT, context)

        if not input_csv:
            raise QgsProcessingException(
                self.tr('Nenhum arquivo CSV foi informado.')
            )

        if not os.path.exists(input_csv):
            raise QgsProcessingException(
                self.tr('Arquivo não encontrado: {}').format(input_csv)
            )

        # Ler cabeçalho bruto do CSV
        header, delimiter = self._read_header(input_csv)
        feedback.pushInfo(self.tr('Cabeçalho do CSV lido com sucesso.'))
        feedback.pushInfo(self.tr('Delimitador detectado: "{}"').format(delimiter))
        feedback.pushInfo(self.tr('Campos detectados: {}').format(', '.join(header)))

        # Aceita nomes alternativos do WKT
        wkt_candidates = ['GEOMETRIA_WKT', 'WKT', 'GEOMETRIA', 'GEOM', 'geometry', 'geom']
        z_candidates = ['Z', 'COTA', 'ALTURA', 'H']

        wkt_field = self._find_field_name(header, wkt_candidates)
        z_field = self._find_field_name(header, z_candidates)

        if not wkt_field:
            raise QgsProcessingException(
                self.tr(
                    "O CSV não possui um campo de geometria WKT reconhecido. "
                    "Campos aceitos: {}."
                ).format(', '.join(wkt_candidates))
            )

        # Criar camada a partir do campo WKT encontrado
        uri = 'file:///{path}?delimiter={delim}&crs=epsg:4674&wktField={wkt}'.format(
            path=input_csv.replace('\\', '/'),
            delim=delimiter,
            wkt=wkt_field
        )

        source = QgsVectorLayer(uri, 'vertice', 'delimitedtext')

        if not source.isValid():
            raise QgsProcessingException(
                self.tr('Arquivo CSV não pôde ser carregado como camada delimitedtext.')
            )

        feedback.pushInfo(self.tr('Arquivo CSV lido com sucesso.'))

        feat_count = source.featureCount()
        if feat_count == 0:
            raise QgsProcessingException(
                self.tr('O CSV não possui feições para processamento.')
            )

        # Checagem do tipo geométrico da camada
        source_wkb = source.wkbType()
        source_geom_type = QgsWkbTypes.geometryType(source_wkb)

        if source_geom_type == QgsWkbTypes.PolygonGeometry:
            raise QgsProcessingException(
                self.tr(
                    'O CSV possui geometria do tipo {}. '
                    'Esta ferramenta aceita apenas geometrias POINT.'
                ).format(self._display_geom(source_wkb))
            )

        if source_geom_type == QgsWkbTypes.LineGeometry:
            raise QgsProcessingException(
                self.tr(
                    'O CSV possui geometria do tipo {}. '
                    'Esta ferramenta aceita apenas geometrias POINT.'
                ).format(self._display_geom(source_wkb))
            )

        if source_geom_type == QgsWkbTypes.UnknownGeometry:
            feedback.pushInfo(
                self.tr(
                    'A camada possui tipo geométrico indefinido. Será feita validação feição a feição.'
                )
            )
        elif source_geom_type != QgsWkbTypes.PointGeometry:
            raise QgsProcessingException(
                self.tr(
                    'Geometria não suportada: {}. Esta ferramenta aceita apenas POINT.'
                ).format(self._display_geom(source_wkb))
            )

        if not z_field:
            raise QgsProcessingException(
                self.tr(
                    "O CSV não possui um campo Z reconhecido. "
                    "Campos aceitos: {}."
                ).format(', '.join(z_candidates))
            )

        feedback.pushInfo(self.tr('Campo WKT identificado: {}').format(wkt_field))
        feedback.pushInfo(self.tr('Campo Z identificado: {}').format(z_field))
        
        # Criar saída PointZ
        out_fields = source.fields()

        sink, dest_id = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            out_fields,
            QgsWkbTypes.PointZ,
            source.sourceCrs()
        )

        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        total = 100.0 / feat_count if feat_count else 0
        total_ok = 0
        total_skip = 0

        for current, feature in enumerate(source.getFeatures()):

            if feedback.isCanceled():
                break

            geom = feature.geometry()

            if geom is None or geom.isEmpty():
                total_skip += 1
                feedback.pushInfo(
                    self.tr('Feição {} ignorada: geometria nula ou vazia.').format(current + 1)
                )
                feedback.setProgress(int(current * total))
                continue

            feature_geom_type = QgsWkbTypes.geometryType(geom.wkbType())
            if feature_geom_type != QgsWkbTypes.PointGeometry:
                total_skip += 1
                feedback.pushInfo(
                    self.tr(
                        'Feição {} ignorada: geometria {} não é Point.'
                    ).format(current + 1, self._display_geom(geom.wkbType()))
                )
                feedback.setProgress(int(current * total))
                continue

            try:
                pt = geom.asPoint()
                x = float(pt.x())
                y = float(pt.y())
            except Exception as e:
                total_skip += 1
                feedback.pushInfo(
                    self.tr(
                        'Feição {} ignorada: erro ao converter geometria em Point ({})'
                    ).format(current + 1, str(e))
                )
                feedback.setProgress(int(current * total))
                continue

            try:
                z = self._parse_z_value(feature[z_field])
            except Exception as e:
                total_skip += 1
                feedback.pushInfo(
                    self.tr(
                        'Feição {} ignorada: valor inválido no campo {} ({})'
                    ).format(current + 1, z_field, str(e))
                )
                feedback.setProgress(int(current * total))
                continue

            try:
                new_feature = QgsFeature(out_fields)
                new_feature.setAttributes(feature.attributes())
                new_feature.setGeometry(QgsGeometry(QgsPoint(x, y, z)))
                sink.addFeature(new_feature, QgsFeatureSink.FastInsert)
                total_ok += 1
            except Exception as e:
                total_skip += 1
                feedback.pushInfo(
                    self.tr(
                        'Feição {} ignorada: erro ao criar PointZ ({})'
                    ).format(current + 1, str(e))
                )

            feedback.setProgress(int(current * total))

        if total_ok == 0:
            raise QgsProcessingException(
                self.tr(
                    'Nenhuma feição válida pôde ser convertida para PointZ.'
                )
            )

        feedback.pushInfo(
            self.tr(
                'Processamento concluído. Feições convertidas: {}. Feições ignoradas: {}.'
            ).format(total_ok, total_skip)
        )

        return {self.OUTPUT: dest_id}