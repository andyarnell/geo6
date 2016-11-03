#script to export maps rasters one by one to as png/pdf
#created for geo-6 mapping wokrshop in July 2015
import arcpy
import os
import time
#list workspaces for inputs and outputs
arcpy.env.overwriteOutput = True


beginTime=time.clock()
####name of admin layer to keep displaying

#adminLyr='Africa Region'
#adminLyr='Asia and Pacific Region'
#adminLyr='Europe Region'
#adminLyr='Latin America and Caribbean Region'
adminLyr='West Asia Region'

####list workspaces for inputs and outputs
#Define outpath and workspace
outPath = r"P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\Maps\Final_Maps\WA"
arcpy.env.workspace = outPath

####Set the mxd:
#mxd = arcpy.mapping.MapDocument("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/outputs/outputs/MXD/Africa/Africa_5.mxd")
#mxd = arcpy.mapping.MapDocument("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/outputs/outputs/MXD/AP/AsiaPacific_4.mxd")
#mxd = arcpy.mapping.MapDocument("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/outputs/outputs/MXD/EU/EUROPE_1.mxd")
#mxd = arcpy.mapping.MapDocument("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/outputs/outputs/MXD/LAC/LAC_2.mxd")
mxd = arcpy.mapping.MapDocument("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/outputs/outputs/MXD/WA/WestAsia_2.mxd")

#mxd = arcpy.mapping.MapDocument("CURRENT")


#Create a fresh layer list
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
        layers=arcpy.mapping.ListLayers(mxd,"*", df) 
print layers


#Export the maps:
print "Exporting maps for each layer"
#turn all layers off except ones on permanently
for layer in layers:
    if layer.name== adminLyr or layer.name=='Other countries' or layer.name=="background":
        layer.visible=True
    else:
        layer.visible=False

arcpy.RefreshTOC()
arcpy.RefreshActiveView()



for layer in layers:
    layer.visible=True
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
    if layer.name== adminLyr or layer.name=='Other countries' or layer.name=="background" or layer.name=="All species - mammals, amphibians and birds" or layer.name=="Modelled land use 2050"  or layer.name=="Modelled land use: 2005":
        print "skipping  printing layer"
    else:
        out_png=outPath + "/"+ str(layer)+".png"
        try:
            print out_png
            #arcpy.mapping.ExportToPNG(mxd,out_png,resolution=600)
            arcpy.mapping.ExportToPDF(mxd,out_png,resolution=300)
            print "printing to file", layer
        except:
            print 'failed to write map'
            pass
    if layer.name== adminLyr or layer.name=='Other countries' or layer.name=="background":
        layer.visible=True
    else:
        layer.visible=False
    
print "Finished processing"
print("Total elapsed time (minutes): " + str((time.clock() - beginTime)/60))

    
    



