# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsFeature,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorLayer)
from qgis import processing


class addFeat(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return addFeat()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'addFeat'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Adicionar vertices SIGEF')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return ''

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Camada SIGEF'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.OUTPUT,
                self.tr('Camada para Adicionar Dado'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source_in = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )
        if not source_in:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))
        
            
        source_out = self.parameterAsVectorLayer(
            parameters,
            self.OUTPUT,
            context
        )
        if not source_out:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.OUTPUT))
        
        total = 100.0 / source_in.featureCount() if source_in.featureCount() else 0
        
        for current, feature in enumerate(source_in.getFeatures()):
            feat = QgsFeature(source_out.fields())
            feat.setAttribute('sigma_x', float(feature['sigma_x']))
            feat.setAttribute('sigma_y', float(feature['sigma_y']))
            feat.setAttribute('sigma_z', float(feature['sigma_z']))
            feat.setAttribute('metodo_pos',feature['metodo_pos'])
            feat.setAttribute('vertice',feature['vertice'])
            feat.setAttribute('tipo_verti',feature['tipo_verti'])
            feat.setAttribute('qrcode',feature['qrcode'])
            feat.setGeometry(feature.geometry())
            (res, outFeats) = source_out.dataProvider().addFeatures([feat])
            feedback.setProgress(int(current * total))
        
        i=0
        for feature in source_out.getFeatures():
            i+=1
            attrs = { 0 : i}
            source_out.dataProvider().changeAttributeValues({ feature.id() : attrs })
        
        source_out.triggerRepaint()
        
        
            
        return {}
