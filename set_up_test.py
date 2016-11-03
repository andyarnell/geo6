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

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "wgs84 grid_half_degree"
arcpy.CreateFishnet_management(out_feature_class="C:/Data/geo6/raw/grids/wgs84 grid_half_degree.shp",origin_coord="-180 -90",y_axis_coord="-180 -80",cell_width="0.5",cell_height="0.5",number_rows="0",number_columns="0",corner_coord="180 90",labels="LABELS",template="wgs84 grid_half_degree",geometry_type="POLYGON")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "wgs84 grid_half_degree"
arcpy.CalculateField_management(in_table="wgs84 grid_half_degree",field="cell_id",expression="[FID]+1
",expression_type="VB",code_block="#")


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "wgs84 grid_half_degree"
arcpy.AddField_management(in_table="wgs84 grid_half_degree",field_name="cell_id",field_type="LONG",field_precision="#",field_scale="#",field_length="#",field_alias="#",field_is_nullable="NULLABLE",field_is_required="NON_REQUIRED",field_domain="#")


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "fields_all_future_africa"
arcpy.TabulateIntersection_analysis(in_zone_features="C:/Data/geo6/raw/grids/wgs84 grid_half_degree.shp",zone_fields="cell_id",in_class_features="fields_all_future_africa",out_table="C:/Data/geo6/scratch/fields_future_tab_int_halfdeg_test.dbf",class_fields="#",sum_fields="#",xy_tolerance="#",out_units="SQUARE_KILOMETERS")
