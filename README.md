# XArrayAndRasterio
Experimental code for loading/saving XArray DataArrays to Geographic Rasters using rasterio

Requirements:
  - `xarray`
  - `numpy`
  - `rasterio`
  - `pandas`
  
Functions provided:
  - `xarray_to_rasterio`: Allows you to export an xarray DataArray to a rasterio-compatible file (GeoTIFF mainly)
  - `rasterio_to_xarray`: Allows you to read any rasterio-compatible file into an xarray DataArray
  - `xarray_to_rasterio_by_band`: Same as `xarray_to_rasterio` but exports one file per band

Author: Robin Wilson (robin@rtwilson.com). Experimental code!
