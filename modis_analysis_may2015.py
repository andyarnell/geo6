##aim: analyse hansen data
##created by Andy Arnell 09/06/2015

print "Importing packages"

import os
import arcpy
from arcpy import env
from arcpy.sa import *
import glob
import string

import time

print "Setting local parameters and inputs"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

env.overwriteOutput = True

beginTime = time.clock()

arcpy.env.overwriteOutput = True 
#Set environment settings

# Check out Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

rawFolder = "C:/Data/geo6/raw/forest/tifs"

tempFolder = "C:/Data/geo6/scratch/modis_working" 

reclFolder=tempFolder+"/reclass/"

aggFolder=tempFolder+"/aggregate/"

outFolder=tempFolder+"/output/"

outFName="modis_vcf2010_halfdeg_all.tif"


#for names in listNames:
env.workspace = rawFolder+"/"
raster_list = arcpy.ListRasters()
#raster_list = [os.path.basename(x) for x in glob.glob(rawFolder+"/" + "/*.tif)]
dataset = rawFolder+"/" + raster_list[0]
spatial_ref = arcpy.Describe(dataset).spatialReference
#cellSize=arcpy.GetRasterProperties_management(dataset,"CELLSIZEX")
#print "test with two tiles"
#raster_list = raster_list[0:15]
print "Raster list from folder, contains the following files:" + str(raster_list)


beginTime1 = time.clock()

aggVal=240 #amount to aggregate pixels

print "Reclassifying rasters - water pixels to nulls"

#for raster in raster_list:
#    inRaster = Raster(raster)
#    OutRaster = SetNull(inRaster>100,inRaster)
#    reclOut=reclFolder+raster+".tif"
#    print "Reclassified raster:" +str(raster)
#    OutRaster.save(reclOut)

print("Elapsed time (minutes): " + str((time.clock() - beginTime1)/60))

beginTime2 = time.clock()

#set new workspace and make new raster list
env.workspace = reclFolder
raster_list = arcpy.ListRasters()

print "Aggregating  rasters by factor: " + str(aggVal)
#for raster in raster_list:
#    outAggreg = Aggregate(raster, aggVal, "MEAN", "EXPAND", "DATA")
#    outAggreg.save(aggFolder+str(raster))
#    print "Aggegated raster: " +str(raster)

print("Elapsed time (minutes): " + str((time.clock() - beginTime2)/60))

beginTime3 = time.clock()

print "Mosaic files to new raster"
#set new workspace and make new raster list
env.workspace = aggFolder
raster_list = arcpy.ListRasters()
arcpy.MosaicToNewRaster_management(raster_list,outFolder,outFName,"#", pixel_type="32_BIT_FLOAT",cellsize="#",number_of_bands="1",mosaic_method="MEAN",mosaic_colormap_mode="MATCH")

print("Elapsed time (minutes): " + str((time.clock() - beginTime3)/60))


print "Finished processing"

print("Total elapsed time (minutes): " + str((time.clock() - beginTime)/60))



