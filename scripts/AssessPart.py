## Assess Part
import processing
DataDir = r'C:/Data/'
for varYear in range(2001, 2017):
	targetLyr = QgsVectorLayer(DataDir + 'Parcels' + str(varYear) + '.shp', 'Parcels' + str(varYear) + "'", 'ogr')
	inLyr = QgsVectorLayer(DataDir + 'HASSESS.DBF', 'HASSESS', 'ogr')
	inLyr.setSubsetString('"FINYEAR" = ' + str(varYear))
	targetField = 'PIN'
	inField = 'MAPBLOLOT'
	result = processing.runalg('qgis:joinattributestable', targetLyr, inLyr, targetField, inField, None)
	load_it = QgsVectorLayer(result['OUTPUT_LAYER'], str(varYear)+ 'join', 'ogr')
	QgsMapLayerRegistry.instance().addMapLayer(load_it)
	inputClip = str(varYear) + 'join'
	clipClip = DataDir + 'rev_share_1980_DEB_StatePlane.shp'
	outputClip = DataDir + 'AssessClip' + str(varYear) + '.shp'
	processing.runalg("qgis:clip", inputClip, clipClip, outputClip)
	loadanother = QgsVectorLayer(outputClip, 'AssessClip' + str(varYear), 'ogr')
	QgsMapLayerRegistry.instance().addMapLayer(loadanother)
