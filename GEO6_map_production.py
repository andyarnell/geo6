import arcpy

beginTime = time.clock()

#set to overwrite existing outputs
arcpy.env.overwriteOutput = True
#list workspaces for inputs and outputs
myWorkspace=r"C:\Data\GEO6\Final_Maps\Africa"
arcpy.env.workspace = myWorkspace

############################################################
#Create lists of layers in current data frame
mxd = arcpy.mapping.MapDocument('CURRENT')
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
            layers=arcpy.mapping.ListLayers(mxd,"*", df) 
            #for layer in layers:
               # if layer not in  NonList:
                   # LayerList.append(layer)
layers=layers[1:17]


#State output path

outPath = "C:/Data/GEO6/Final_Maps/Africa" 
#Eulayer=arcpy.mapping.ListLayers(mxd,"Europe", df) 

#Retrieve the symbology from existing layer files:
#Create path to each layer file:

    
#Build loop to change the names of the raster layers
for layer in layers:
    if layer.name  == str("MODIS_VCF_2010_clean_scaled"):
        newname = str("Tree cover (%)")
        layer.name = newname
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers:
    if layer.name  == str("Mines_all_prosp"):
        newname = str("Count of early-stage development mines")
        layer.name = newname
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers:
    if layer.name  == str("Mines_all_futur"):
        newname = str("Count of late-stage development mines")
        layer.name = newname
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers:
    if layer.name  == str("Mines_all_curre"):
        newname = str("Count of current mines")
        layer.name = newname
arcpy.RefreshActiveView()
arcpy.RefreshTOC()   

for layer in layers:
    if layer.name  == str("GPWv4_0"):
        newname = str("Human population density (persons per km sq)")
        layer.name = newname   
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers:
    if layer.name  == str("Fields_all_over"):
        newname = str("Area of overlap of future and current fields (oil&gas)")
        layer.name = newname    
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers:    
    if layer.name  == str("Fields_all_futu"):
        newname = str("Area of future fields (oil&gas)")
        layer.name = newname    
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
    
for layer in layers:  
    if layer.name  == str("Fields_all_curr"):
        newname = str("Area of current fields (oil&gas)")
        layer.name = newname    
arcpy.RefreshActiveView()
arcpy.RefreshTOC()   

for layer in layers:  
    if layer.name  == str("all_oil_gas_pip"):
        newname = str("Length of pipelines (oil&gas)")
        layer.name = newname    
arcpy.RefreshActiveView()
arcpy.RefreshTOC()   

for layer in layers: 
    if layer.name  == str("AbovegroundBiomassCarbon_Lay1_halfd_sumi"):
        newname = str("Total Above Ground Biomass Carbon (ha)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC()  

for layer in layers: 
    if layer.name  == str("Wat_yield_NC"):
        newname = str("Freshwater resources (mm)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC() 

for layer in layers: 
    if layer.name  == str("sprich_mab"):
        newname = str("Species richness: mammals, amphibians, birds (number of species)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC() 

for layer in layers: 
    if layer.name  == str("rrarity_mab_avg"):
        newname = str("Mean range-size rarity: mammals, amphibians and birds")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC() 

for layer in layers: 
    if layer.name  == str("glues_cropsuit_recent_1981_2010_halfdeg"):
        newname = str("Current agricultural suitability (1981-2010)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC() 

for layer in layers: 
    if layer.name  == str("glues_cropsuit_future_2011_2040_halfdeg"):
        newname = str("Future agricultural suitability (2011-2040)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers: 
    if layer.name  == str("all_rast_future_dev_corr_infr_binary"):
        newname = str("Future development corridors")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
     
#update their symbology:
   
#Create new list of layers with their new names
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
            layers=arcpy.mapping.ListLayers(mxd,"*", df) 
            #for layer in layers:
               # if layer not in  NonList:
                   # LayerList.append(layer)
layers=layers[1:17]
print layers
#Source layer files
lyrFile1 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Total Above Ground Biomass Carbon (ha).lyr")
lyrFile2 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Length of pipelines (oil&gas).lyr")
lyrFile3 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Area of current fields (oil&gas).lyr")
lyrFile4 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Area of overlap of future and current fields (oil&gas).lyr")
lyrFile5 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Count of late-stage development mines.lyr")
lyrFile6 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Count of future mines.lyr")
lyrFile7 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Count of early-stage development mines.lyr")
lyrFile8 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Human population density (persons per km sq).lyr")
lyrFile9 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Tree cover (%).lyr")
lyrFile10 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Area of future fields (oil&gas).lyr")
lyrFile11 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Mean range-size rarity for mammals, amphibians and birds.lyr")
lyrFile12 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Future agricultural suitability (2011-2040).lyr")
lyrFile13 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Current agricultural suitability (1981-2010).lyr")
lyrFile14 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Future development corridors.lyr")
lyrFile15 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Species richness of mammals, amphibians and birds (number of species).lyr")
lyrFile16 = arcpy.mapping.Layer(r"C:\Data\GEO6\Final_Maps\Template_design\Freshwater resources (mm).lyr")

# update the symbology of re-named rasters with the layer files

df = arcpy.mapping.ListDataFrames(mxd)[0]
updateLayer = arcpy.mapping.ListLayers(mxd, "Total*", df)
sourceLayer = lyrFile1
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Length*", df)
sourceLayer = lyrFile2
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Area of current*", df)
sourceLayer = lyrFile3
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Area of overlap*", df)
sourceLayer = lyrFile4
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Count of current*", df)
sourceLayer = lyrFile5
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Count of future*", df)
sourceLayer = lyrFile6
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Count of prospective*", df)
sourceLayer = lyrFile7
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Human population*", df)
sourceLayer = lyrFile8
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Tree*", df)
sourceLayer = lyrFile9
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Area of future*", df)
sourceLayer = lyrFile10
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Mean range-size*", df)
sourceLayer = lyrFile11
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Future agricultural*", df)
sourceLayer = lyrFile12
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Current agricultural*", df)
sourceLayer = lyrFile13
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"   
updateLayer = arcpy.mapping.ListLayers(mxd, "Future development*", df)
sourceLayer = lyrFile14
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"    
updateLayer = arcpy.mapping.ListLayers(mxd, "Species richness*", df)
sourceLayer = lyrFile15
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"    
updateLayer = arcpy.mapping.ListLayers(mxd, "Freshwater resources*", df)
sourceLayer = lyrFile16
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"     
#========================================================================================================================================   
#set to overwrite existing outputs
arcpy.env.overwriteOutput = True
import arcpy
import os
import time
#list workspaces for inputs and outputs
arcpy.env.overwriteOutput = True

#list workspaces for inputs and outputs
#myWorkspace="C:/Data/GEO6/Final_Maps/EU" 
arcpy.env.workspace = "C:/Data/GEO6/Final_Maps/Africa"
#Define outpath
outPath = "C:/Data/GEO6/Final_Maps/Africa" 
#Set the mxd:
mxd = arcpy.mapping.MapDocument("C:/Data/GEO6/Final_Maps/Africa/Africa.mxd")
#Create a fresh layer list
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
        layers=arcpy.mapping.ListLayers(mxd,"*", df) 
#Export the maps:

arcpy.RefreshTOC()
arcpy.RefreshActiveView()

print "Exporting maps for each layer"

for layer in layers:
    if layer.name=='Africa' or layer.name=='Other countries':
        layer.visible=True
    else:
        layer.visible=False
    layer.visible=True
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
    out_png=outPath + "/test"+ str(layer)+".png"
    try:
        print out_png
        arcpy.mapping.ExportToPNG(mxd,out_png,resolution=600)
        arcpy.mapping.ExportToPDF(mxd,out_png,resolution=600)
        print "printing to file", layer
    except:
        print 'failed to write map'
        pass
    layer.visible=False
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
        #del (mxd)
    
print "Finished processing"
print("Total elapsed time (minutes): " + str((time.clock() - beginTime)/60))

    
    



