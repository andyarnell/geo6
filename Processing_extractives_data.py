#Python code for ArcMap 10.2, Python v 2.7
# Code development by Brian O' Connor June 2015
import sys, os
import os
import arcpy
from arcpy import env
import time

beginTime = time.clock()

#set to overwrite existing outputs
arcpy.env.overwriteOutput = True

#set workspace for inputs and outputs
myWorkspace="C:\Data\GEO6\Extractives_Map\Global_Geodatabase.gdb"
arcpy.env.workspace = myWorkspace
#env.outputCoordinateSystem = r"C:\Users\briano\AppData\Roaming\ESRI\Desktop10.2\ArcMap\Coordinate Systems\WGS 1984.prj"

#Set enviroenment extent
#arcpy.env.extent = 'C:\Data\GEO6\Extractives_Map\EU_geodatabase.gdb\EU_boundary'

#Point_feature_type='Point'
fclist = arcpy.ListFeatureClasses()
#Point_fclist = arcpy.ListFeatureClasses("trans_*",Point_feature_type,"")
    
#Intersect transport layers with the grid
#Note - the grid should be in an equal area projection, e.g. Mercator for later calcs
# Set up loop for points and polygons

countLine=0
countPoint=0
countArea=0
countOther=0
Parser="_intersect"
for feature in fclist:
    lastchar = feature[-1]
    if lastchar=='p':
       countPoint=countPoint+1
       inFeatures = [feature, "wgs84_grid_half_degree"]
       arcpy.Intersect_analysis(inFeatures, feature + Parser,"ONLY_FID","#","POINT")
        
    if lastchar=='l':
       countLine=countLine+1
       inFeatures = [feature, "wgs84_grid_half_degree"]
       arcpy.Intersect_analysis(inFeatures, feature + Parser, "ONLY_FID", "","LINE")

    elif lastchar=='a':
        countArea=countLine+1
        inFeatures = [feature, "wgs84_grid_half_degree"]
        arcpy.Intersect_analysis(inFeatures, feature + Parser, "ONLY_FID", "","INPUT")
    
    #else:
        #countOther=countOther+1
print fclist
print countLine,"line features have been intersected,",countPoint,"point features have been intersected and", countArea,"polygon features have been intersected" #countOther "features remain in the workspace"


#Make a separate list of the intersected point and line layers
feature_type_line='Polyline'
feature_type_point='Point'
feature_type_area='Polygon'
fclistLine = arcpy.ListFeatureClasses("*_intersect",feature_type_line,"")
fclistPoint = arcpy.ListFeatureClasses("*_intersect",feature_type_point,"")
fclistArea = arcpy.ListFeatureClasses("*_intersect",feature_type_area,"")

# Project layers to an equidistant projection for correct calculation of length (note - only need to do this for line files):
#NOTE- this step has been omitted and replaced with a geodesic length calculation
for feature in fclistLine:
    arcpy.AddGeometryAttributes_management(feature,Geometry_Properties="LENGTH_GEODESIC",Length_Unit="KILOMETERS",Area_Unit="#",Coordinate_System="#")
print "Geodesic length calculated for", feature

for feature in fclistArea:
    arcpy.AddGeometryAttributes_management(feature,Geometry_Properties="AREA_GEODESIC",Length_Unit="",Area_Unit="SQUARE_KILOMETERS",Coordinate_System="#") 
print "Geodesic area calculated for", feature
   
# calculate summary stats and output a table
# for lines
count=0
for feature in fclistLine:
    count=count+1
    #Generate stats table
    arcpy.Statistics_analysis(feature,feature+"_sum_table_l","LENGTH_GEO SUM","FID_wgs84_grid_half_degree")
    print count, " sum line tables written to file"
# for areas
count=0  
for feature in fclistArea:
    count=count+1
    #Generate stats table
    arcpy.Statistics_analysis(feature,feature+"_sum_table_a","AREA_GEO SUM","FID_wgs84_grid_half_degree")
    print count, " sum area tables written to file"

#For points - need to count the number of points in the grid cell, i.e. frequency
count=0
FieldNameList=[]
for feature in fclistPoint:
    #parsing the field name for stats calc from the file name 
    count=count+1
    FieldName=fclistPoint[count-1:count] 
    for i in FieldName:
        x=i.find('_intersect')
        statsField = "FID_"+i[0:x]
        #statsFieldStr= statsField.encode('utf8')
        print   statsField
        FieldNameList.append(statsField)
        print FieldNameList
    #Generate 2-way matrix of file name and field name
zipped = zip (fclistPoint,FieldNameList)
count=0
for i,j in zip(fclistPoint,FieldNameList):
    statsFields = [[j, "COUNT"]]
    arcpy.Statistics_analysis(i,i+ "_count_table", statsFields,"FID_wgs84_grid_half_degree")
    count=count+1
    print count, " count point tables written to file"    

# Join the count and sum fields back to the original grid cells (using FID) via a table join
#for lines
Tablelist = arcpy.ListTables("*_sum_table_l")
# Set the local parameters:
#for lines
indata = "wgs84_grid_half_degree"
in_field="OBJECTID"
joinField = "FID_wgs84_grid_half_degree"
fieldList = ["SUM_LENGTH_GEO"]
print"Joining line distance tables to the original grid"
for table in Tablelist:
    try:
        arcpy.JoinField_management (indata, in_field, table, joinField, fieldList)
        print "joined %s successfully" % table
    except:
        print arcpy.GetMessages()
        break

#for areas
Tablelist = arcpy.ListTables("*_sum_table_a")
indata = "wgs84_grid_half_degree"
in_field="OBJECTID"
joinField = "FID_wgs84_grid_half_degree"
fieldList = ["SUM_AREA_GEO"]
print "Joining area tables to the original grid"
for table in Tablelist:
    try:
        arcpy.JoinField_management (indata, in_field, table, joinField, fieldList)
        print "joined %s successfully" % table
    except:
        print arcpy.GetMessages()
        break
#for points    
Tablelist = arcpy.ListTables("*_count_table")
# Set the local parameters
indata = "wgs84_grid_half_degree"
in_field="OBJECTID"
joinField = "FID_wgs84_grid_half_degree"
fieldList = ["FREQUENCY"]
print "Joining point frequency tables to the original grid"
for table in Tablelist:
    try:
        arcpy.JoinField_management (indata, in_field, table, joinField, fieldList)
        print "joined %s successfully" % table
    except:
        print arcpy.GetMessages()
        break

#Create list of file names and field names
FileNameList= fclistLine + fclistArea + fclistPoint
#FieldNames = arcpy.ListFields("wgs84_grid_half_degree")
FieldNameList = [f.name for f in arcpy.ListFields("wgs84_grid_half_degree")]

#for field in FieldNames:
   # FieldNameList =  field.name
FieldNameList= FieldNameList[6:]

z = zip(FileNameList,FieldNameList)
count = 0

for i,j in z:
    count = count+1
    i=i[:15]
    arcpy.PolygonToRaster_conversion("wgs84_grid_half_degree",j,i,"#","#",0.5)  
    print "Exported field "+ j + " to file: " + i + ",raster: " + str(count)
print count, "rasters exported"
#delete unnecessary feature classes 
dataType="#"
#Create safe list of files for non-deletion
SaveFiles=["wgs84_grid_half_degree","WA_boundary", "Mines_all_prospect_p", "all_oil_gas_pipes_l", "Mines_all_future_p","Mines_all_current_p","Fields_all_overlap_futureincurrent_diss_a","Fields_all_future_dissolve_a","Fields_all_current_dissolve_a"]
#Create list of files to delete
DeleteList=[]
for feature in fclist:
    if not feature in SaveFiles:
        DeleteList.append (feature)
    else:
        pass
for item in DeleteList:
    arcpy.Delete_management(item, dataType)
    print "%s deleted" % (item)

#delete unnecessary tables 
tables = arcpy.ListTables()
for table in tables:
    arcpy.Delete_management(table, dataType)  
    print "%s deleted" % (table)    

print ("Total elapsed time (seconds): " + str(time.clock() - beginTime))
