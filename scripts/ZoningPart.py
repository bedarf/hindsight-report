## Zoning Part
import processing
DataDir = r'C:/Data/'
for zoningYear in range(2002, 2016):
	print zoningYear
	inputClip = DataDir + 'Zoning' + str(zoningYear) + '.shp'
	print inputClip
	clipClip = DataDir + 'rev_share_1980_DEB_StatePlane.shp'
	outputClip = DataDir + 'ZoningClip' + str(zoningYear) + '.shp'
	outputDissolve = DataDir + 'ZoningDissolve' + str(zoningYear) + '.shp'
	outputDissolveArea = DataDir + 'ZoningDissolveArea' + str(zoningYear) + '.shp'
	processing.runalg("qgis:clip", inputClip, clipClip, outputClip)
	processing.runalg("qgis:dissolve", outputClip, False, "ZONING", outputDissolve)
	processing.runalg("qgis:fieldcalculator", outputDissolve, "Area", 0, 10, 3, True, "$area*0.000247105", outputDissolveArea) # adding area in acres
