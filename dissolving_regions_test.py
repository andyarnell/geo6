print('Importing modules')
import sys
import arcpy
from arcpy import env
from arcpy.sa import *
import time

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

env.overwriteOutput = True

inFolder= r"P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\GIS_Analysis\raw\admin_boundaries\UNEP_regions"
outFolder = r"C:\Data\geo6\scratch"

beginTime = time.clock()
print('Dissolving each shapefile seperately')
#arcpy.Dissolve_management(inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_Africa.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AfricaDISS.shp","#","#","MULTI_PART","DISSOLVE_LINES")
#arcpy.Dissolve_management(inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AsiaPacific.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AsiaPacificDISS.shp","#","#","MULTI_PART","DISSOLVE_LINES")
#arcpy.Dissolve_management(inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_Europe.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_EuropeDISS.shp","#","#","MULTI_PART","DISSOLVE_LINES")
#arcpy.Dissolve_management(inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_LAC.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_LACDISS.shp","#","#","MULTI_PART","DISSOLVE_LINES")
#arcpy.Dissolve_management(inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_WestAsia.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_WestAsiaDISS.shp","#","#","MULTI_PART","DISSOLVE_LINES")

print "merging"

#arcpy.Merge_management([inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_Africa.shp", inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AsiaPacific.shp", inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_Europe.shp", inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_LAC.shp", inFolder+"/"+"EEZv8_WVS_DIS_V3_Land_WestAsia.shp"],outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMerge.shp")

print "dissolving by field"
#dissolveField = "GEOandUNEP"
#arcpy.Dissolve_management(outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMerge.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDiss.shp",dissolveField,"#","MULTI_PART","DISSOLVE_LINES")

print "repairing geometry"
arcpy.RepairGeometry_management(outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDiss.shp")

print "dissolving all"
arcpy.Dissolve_management(outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDiss.shp",outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDissToOne.shp","#","#","MULTI_PART","DISSOLVE_LINES")

inFolder= r"P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\GIS_Analysis\raw\admin_grid_templates"

#SelectLayerByLocation_management (inFolder+"/"+"wgs84 grid_half_degree.shp", INTERSECT, outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDissToOne.shp", "#", {selection_type})

joinField=dissolveField

#print "joining attributes to grid"
#SpatialJoin_analysis (inFolder+"/"+"wgs84_grid_half_degree.shp", outFolder+"/"+"EEZv8_WVS_DIS_V3_Land_AllMergeDiss.shp", outFolder+"/"+"wgs84_grid_half_degree_regions.shp", JOIN_ONE_TO_MANY, KEEP_COMMON, joinField, INTERSECTS, "#", "#")

                     
print "Finished processing"
print("Elapsed time (minutes): " + str((time.clock() - beginTime)/60))



