####################################
# Setting up the arcpy environment #
####################################
import arcpy
import os

# Path
path = r"C:\Paige_GIS\NetCDF_To_Tiff\Data"
arcpy.env.workspace = path

# Set the output geodatabase
output_geodatabase = r"C:\Paige_GIS\NetCDF_To_Tiff\NetCDF_To_Tiff.gdb"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = False

# Print statement to check the contents of the input folder
print(f"Contents of {path}: {os.listdir(path)}")

# Generate a list of all raster files in the folder with ".nc" extension
nc_list = [file for file in os.listdir(path) if file.endswith('.nc')]

# Print statement to check if any NC files are found
print(f"Found {len(nc_list)} NC files.")

# Loop through each nc file
for file in nc_list:
    # Construct the full path to the input nc file
    input_nc = os.path.join(path, file)

    # Construct the layer name dynamically based on the file name
    layer_name = os.path.splitext(file)[0]  # Remove the extension to use as layer name

    # Process: Make NetCDF Raster Layer (Make NetCDF Raster Layer) (md)
    out_raster_layer = os.path.join(output_geodatabase, layer_name)  # Create a unique name for the output layer
    arcpy.md.MakeNetCDFRasterLayer(input_nc, variable="tasmax_tavg", x_dimension="lon", y_dimension="lat",
                                   out_raster_layer=out_raster_layer)


    print(f"Conversion completed for: {file}")