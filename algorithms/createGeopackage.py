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
                       QgsProcessingException,
                       QgsVectorLayer,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFileDestination)
from qgis import processing
import os
import shutil


class createGeopackage(QgsProcessingAlgorithm):
  
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return createGeopackage()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createGeopackage'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Create GeoPackage')

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

        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT,
                self.tr('Destination GeoPackage'),
                self.tr('GeoPackage files (*.gpkg)')
            )
        )


    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        output = self.parameterAsOutputLayer(
            parameters, 
            self.OUTPUT, 
            context)
        if not output:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.OUTPUT))
        
        
        #path_to_gpkg = os.path.dirname(__file__) + "/shp" + "/seed.gpkg"
        fonte = os.path.dirname(__file__) + "/shp" + "/seed.gpkg"
        shutil.copy(fonte, output)
        
        # Check for cancelation
        if feedback.isCanceled():
            return {}
        
        return {self.OUTPUT: output}
    
