# Countywide zoning Stats
import processing
DataDir = r'C:/Data/'
for zoningYear in range(2002, 2016):
	print zoningYear
	inputZoning = DataDir + 'Zoning' + str(zoningYear) + '.shp'
	print inputZoning
	outputZoning = DataDir + 'ZoningALLDissolve' + str(zoningYear) + '.shp'
	outputZoningArea = DataDir + 'ZoningALLDissolveArea' + str(zoningYear) + '.shp'
	processing.runalg("qgis:dissolve", inputZoning, False, "ZONING", outputZoning)
	processing.runalg("qgis:fieldcalculator", outputZoning, "Area", 0, 10, 3, True, "$area*0.000247105", outputZoningArea) # adding area in acres	
