print "importing packages"
import arcpy
import os
import time
import glob
print "Setting local parameters and inputs"

beginTime = time.clock()

arcpy.env.overwriteOutput = True

#choose region to direct in and out "AFR", "AP", "EU", "LAC", "WA"
region="AFR"

#Set file name and remove if it already exists
outPdfPath = "P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/Maps/Final_Maps/"+region+"/combined/Supporting_GEO6-maps.pdf"
print outPdfPath
inPdfPath= "P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/Maps/Final_Maps/"+region
print inPdfPath
#list workspaces for inputs and outputs
arcpy.env.workspace = inPdfPath

extrasPath = r"P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\Maps\extra_pages"
#####choose region page
regionTitle = "Map_docs_title_AF.pdf"
#regionTitle = "Map_docs_title_AP.pdf"
#regionTitle = "Map_docs_title_EU.pdf"
#regionTitle = "Map_docs_title_LAC.pdf"
#regionTitle = "Map_docs_title_WA.pdf"


polPath=r"P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\Maps\Regional and political maps"
######choose region political map
regionPolitMap = "political_Africa.pdf"
#regionPolitMap = "political_AsiaPacific.pdf"
#regionPolitMap = "political_Europe.pdf"
#regionPolitMap = "political_LAC.pdf"
#regionPolitMap = "political_WestAsia.pdf"


if os.path.exists(outPdfPath):
    os.remove(outPdfPath)

#Create the file and append pages
pdfDoc = arcpy.mapping.PDFDocumentCreate(outPdfPath)

#from os.path import isfile, join
#onlyfiles = [ f for f in listdir(inPdfPath) if isfile(join(inPdfPath,f)) ]
pdfList = [os.path.basename(x) for x in glob.glob(inPdfPath+"/*.pdf")]


print "Making list of pdfs in folder"
print "Number of pdfs :" + str(len(pdfList))
i=0                               
for pdf in pdfList:
    print "pdf no: " + str(i) + " Name: " +str(pdf)
    i = i + 1

print "Reordering list of pdfs"

newOrder=[14,11,16,15,6,9,5,7,10,0,1,2,3,4,13,12,8]

newList = [ pdfList[i] for i in newOrder]

print "Number of pdfs :" + str(len(newList))
print "Number of missing pdfs :" + str(len(pdfList)-len(newList))
i=0   
for pdf in newList:
    print "pdf no: "+ str(i) + " Name: " +str(pdf)
    i = i + 1

i=0

for pdf in newList:
    pdfDoc.appendPages(inPdfPath+"/"+pdf)
    print "Appending pdf: " + str(pdf)



print "inserting title page"
pdfDoc.insertPages(extrasPath+"/"+regionTitle,1)


print "inserting political map"
pdfDoc.insertPages(polPath+"/"+regionPolitMap,2)


print "inserting chapter page"
pdfDoc.insertPages(extrasPath+"/"+"es_assets_page.pdf",3)

print "inserting chapter page"
pdfDoc.insertPages(extrasPath+"/"+"pressures_threats_page.pdf",9) 


#Commit changes and delete variable reference
pdfDoc.saveAndClose()
del pdfDoc
