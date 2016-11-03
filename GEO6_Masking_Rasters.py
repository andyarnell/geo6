##Python code for ArcMap 10.2, Python v 2.7
# Code development by Brian O' Connor June 2015
# Code designed to mask rasters by GEO 6 region

# Note that in preparation for this script 2 steps were taken:
#(i): two databases were manually created in the workspace - one for the regional boundary shape files and one for the global rasters to be clipped
#(ii): Once the first part of the script ran - the regional boundary shape file was copied in its respective output database as I didn't have time to write the code to copy the boundary shape file to the workspace as it is
#changed dynamically in the second part of the code
import sys, os
import os
import arcpy
from arcpy import env
import time
from arcpy.sa import *

beginTime = time.clock()

#set to overwrite existing outputs
arcpy.env.overwriteOutput = True
#list workspaces for inputs and outputs
myWorkspace=r"C:\Data\GEO6\Masking"
arcpy.env.workspace = myWorkspace
#=============================================================================================
# First - create a new File GDB for every output masked raster (if it doesn't exist already)

# List all file geodatabases in the current workspace 
workspaces = arcpy.ListWorkspaces("*", "FileGDB")
#Create list of existing databases:
GDBList=[]
x=[]
for workspace in workspaces: 
    GDBList.append(workspace)
# Print workspace name
    for i in GDBList:
        i=i[21:38]
    x.append(i)
#print x
    
# Set Prefixes for new GDB names 
West_Asia = 'WA'
Asia_Pacific = 'AP'
Europe = 'EU'
Latin_America_Caribbean = 'LA'
Africa = 'AF'
Region_List=['WA','AP','EU','LA','AF']

for region in Region_List:
    out_name = region + "_Masked_Results"
    if not out_name in x:
        arcpy.CreateFileGDB_management(myWorkspace,out_name)
        print out_name,".gdb created"
    else:
        pass
        print "Output database ("+out_name+") exists - skipping database creation"
        
#=============================================================================================# 
#Second - take clipping extents from the regional shape file boundaries

myWorkspace = r'C:\Data\GEO6\Masking'
arcpy.env.workspace = myWorkspace
gdbList = arcpy.ListWorkspaces("*", "FileGDB")
#inDir= 'C:\Data\\GEO6\Masking\Masking_Geodatabase.gdb'
#myWorkspace=inDir
x=[]
y=[]
for gdb in gdbList:
    arcpy.env.workspace = gdb               #--change working directory to each GDB in list
    datasetList = arcpy.ListDatasets('*','Raster')     #--make a list of all (if any) feature datasets that exist in current GDB
    fcList = arcpy.ListFeatureClasses()         #--make a list of all feature in current GDB (root)
    if len(fcList)>1:
        x = fcList   
    if len(datasetList)!=0: 
        y=datasetList
print x 
print y

arcpy.CheckOutExtension("Spatial")
    #print datasetList
for gdb in gdbList:
    for fc in x:
        if gdb[21:23]==fc[:2]:
            arcpy.env.workspace = gdb
            for dataset in y:
                outExtractByMask = ExtractByMask(r"C:\Data\GEO6\Masking\Rasters_Geodatabase.gdb"+"/"+dataset, fc) 
                outname = os.path.join(gdb, str(dataset)) # Create the full out path
                outExtractByMask.save(outname)
        else:
            pass

print ("Total elapsed time (seconds): " + str(time.clock() - beginTime))






