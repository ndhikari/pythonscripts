#addingcoordinatesystem
import arcpy
from arcpy import env
env.workspace=r"C:\Users\Roshan\Desktop\HW 10GIS\HW 10 attached files Nov 15, 2019 118 PM\Exercise05"
overwriteOutput=True
in_fc="hospitals.shp"
copied_hospitals= arcpy.Copy_management(in_fc, "hospitals_copied.shp")
arcpy.AddXY_management(copied_hospitals)
print"OK"

