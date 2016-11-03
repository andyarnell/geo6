import arcpy
import time
beginTime = time.clock()

#set to overwrite existing outputs
arcpy.env.overwriteOutput = True

############################################################
#Create lists of layers in current data frame

#mxd = arcpy.mapping.MapDocument(r'C:\Data\geo6\outputs\MXD\Africa\Africa_4.mxd')
mxd = arcpy.mapping.MapDocument('CURRENT')
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
            layers=arcpy.mapping.ListLayers(mxd,"*", df) 
            #for layer in layers:
               # if layer not in  NonList:
                   # LayerList.append(layer)
layers=layers[1:19]

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
        newname = str("Total Above Ground Biomass Carbon")
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
        newname = str("Species richness - mammals, amphibians and birds")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC() 

for layer in layers: 
    if layer.name  == str("rrarity_mab_avg"):
        newname = str("Mean range-size rarity - mammals, amphibians and birds")
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

for layer in layers: 
    if layer.name  == str("GEO6_Non_roads_dens"):
        newname = str("Non-road infrastructure density (km per square km)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

for layer in layers: 
    if layer.name  == str("GEO6_roads_dens"):
        newname = str("Road density (km per square km)")
        layer.name = newname      
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

#############################     
#update their symbology:

#Retrieve the symbology from existing layer files:
  
#Create new list of layers with their new names
for df in arcpy.mapping.ListDataFrames(mxd):
    if (df.name=='Layers'):
            layers=arcpy.mapping.ListLayers(mxd,"*", df) 
            #for layer in layers:
               # if layer not in  NonList:
                   # LayerList.append(layer)
layers=layers[1:19]
print layers
#Source layer files
lyrFile1 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Total Above Ground Biomass Carbon.lyr")
lyrFile2 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Length of pipelines (oil&gas).lyr")
lyrFile3 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Area of current fields (oil&gas).lyr")
lyrFile4 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Area of overlap of future and current fields (oil&gas).lyr")
lyrFile5 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Count of late-stage development mines.lyr")
lyrFile6 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Count of future mines.lyr")
lyrFile7 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Count of early-stage development mines.lyr")
lyrFile8 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Human population density (persons per km sq).lyr")
lyrFile9 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Tree cover (%).lyr")
lyrFile10 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Area of future fields (oil&gas).lyr")
lyrFile11 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Mean range-size rarity - mammals, amphibians and birds.lyr")
lyrFile12 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Future agricultural suitability (2011-2040).lyr")
lyrFile13 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Current agricultural suitability (1981-2010).lyr")
lyrFile14 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Future development corridors.lyr")
lyrFile15 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Species richness - mammals, amphibians and birds.lyr")
lyrFile16 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Freshwater resources (mm).lyr")
lyrFile17 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Non-road infrastructure density (km per square km).lyr")
lyrFile18 = arcpy.mapping.Layer(r"C:\Data\geo6\outputs\Layer Files\Road density (km per square km).lyr")

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
updateLayer = arcpy.mapping.ListLayers(mxd, "Count of late-stage*", df)
sourceLayer = lyrFile6
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Count of early-stage*", df)
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
updateLayer = arcpy.mapping.ListLayers(mxd, "Non-road*", df)
sourceLayer = lyrFile17
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"
updateLayer = arcpy.mapping.ListLayers(mxd, "Road*", df)
sourceLayer = lyrFile18
for lyr in updateLayer:
    arcpy.mapping.UpdateLayer(df, lyr, sourceLayer)
    print lyr, "symbology updated"    
    
print "Finished processing"
print("Total elapsed time (minutes): " + str((time.clock() - beginTime)/60))

    
    



