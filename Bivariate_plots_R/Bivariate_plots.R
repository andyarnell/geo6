
install.packages("Hmisc")
install.packages ("plotrix")
#Choropleth Maps
library(maptools)
gpclibPermit()
library(classInt)
#library(sp)
#library(StatDA)
library(colorspace)
library(grDevices)
#library(fUtilities)
#library(gplots)
library(plotrix)
library(Hmisc)

##Read in the data table. This should be in the format of the id of the square (Grid_ID in teh example) and then the data columns that you are interested in. 
setwd("P:/PROJECTS/7100s/07104.00.E GEO6 Regional Assessments/GIS_Analysis/post_workshop_work/Africa_regional_mapping/scratch/bivariate")
data1.subset<-read.csv("biv_threat_asset.csv", header=T)

#Read in the GIS shapefile that you want to plot. This just needs to have a data table with the corresponding Grid_ID as you need to link to this in a bit. 
map.data <- readShapePoly("Africa_grid_clip.shp")
plot(map.data)

#par( mfrow = c( 1, 2) )

###############################
# Build the data frame  on which the colours are based
#I have done this just with an excel file that has the colors I wanted in. They are RGB values. You could construct one of these yourself or even just produce a straight set of hex labels for the colours. The important thing is that you have an id that corresponds to each square in the colour key that this bit produces. Look at the data and you will see what I mean.  

#Specify the number of categories. This is not used here but later on
n.cat<-10  
#Create a dataframe to use as the basis for the color palette
vector1<-rep(1:n.cat, each=n.cat)
vector2<-rep(1:n.cat, n.cat) 
data.col<-as.data.frame(cbind(vector1, vector2))
col.space<-read.csv("Bivariate Choropleth Sachs Scheme.csv", header=T)
sach.col<-rgb(col.space$R, col.space$G, col.space$B, maxColorValue=255) 
data.col$cat1<-paste(data.col[,1], data.col[,2], sep="")                 
data.col$coln<-sach.col 


#par( mfrow = c( 1, 2))
plot(data.col[,1]~data.col[,2], col=data.col$coln, xlab="Threat", ylab="Biodiversity", pch=15, cex=5)
#plot(data.col[,1]~data.col[,2], col=data.col$coln, xlab="Threat", ylab="Ecosystem assets", pch=15, cex=5)

#################################################################################
#


#Now set the break points for the data
#Option 1 calculate this yourself
brks.1<-classIntervals(data1.subset[,2] , n=n.cat, style="quantile", cutlabels=FALSE)
brks<-brks.1$brks
brks
#Option 2 specify them yourself
#brks<-c(0,0.000001,0.009753, 0.026597, 0.053144, 0.053192, 0.092200, 0.0147164, 0.253547, 0.501774, 1)
#then you cut the data
data1.subset[,4]<-cut(data1.subset[,2], breaks=brks, labels=c(1:n.cat), include.lowest = TRUE)
data1.subset[,4]<-as.numeric(data1.subset[,4])
#Repeat for the other column
brks.2<-classIntervals(data1.subset[,3] , n=n.cat, style="quantile", cutlabels=FALSE)
brks2<-brks.2$brks

brks2

brks2<-c( 0.000000001, 0.000000002, 0.000000003, 0.007695539, 0.101289571, 0.198433912, 0.262052158, 0.303253724, 0.372584553, 0.485038221, 1.000000000)
data1.subset[,5]<-cut(data1.subset[,3] , breaks=brks2, labels=c(1:n.cat), include.lowest = TRUE)
data1.subset[,5]<-as.numeric(data1.subset[,5])
is.numeric(data1.subset[,5])
#NOW the plotting code

#Paste columns 4 and 5 together to get a colour vector
data1.subset[,6]<-paste(data1.subset[,4],data1.subset[,5], sep="")
colnames(data1.subset)[6]<-c("Col.code")
#And merge to get a column with an RGB value 
data.final<-merge(data1.subset, data.col, by.x="Col.code", by.y="cat1") 


#Now merge your shapefile with your data file that has the colour codes. Each grid cell will now have a colour assigned to it. 
map.data@data<-merge(map.data@data, data.final, by.x="CODE", by.y="CODE", all.x=T, sort=F)# set name of ID column used for x and y.

#And plot. 


jpeg(filename="P:\PROJECTS\7100s\07104.00.E GEO6 Regional Assessments\GIS_Analysis\post_workshop_work\Africa_regional_mapping\scratch\bivariate\threat_asset1.jpeg", width=1500, height=1500, quality=100)
plot(map.data, col=map.data$coln, axes=F, border=F)
dev.off()



write.csv(data.final, file ="datafinal.csv",row.names=T)
