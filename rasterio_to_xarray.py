import rasterio
import xarray as xr
import numpy as np


def rasterio_to_xarray(fname):
    """Converts the given file to an xarray.DataArray object"""
    with rasterio.drivers():
        with rasterio.open(fname) as src:
            data = src.read(1)

            # Set values to nan wherever they are equal to the nodata
            # value defined in the input file
            data = np.where(data == src.nodata, np.nan, data)

            # Get coords
            nx, ny = src.width, src.height
            x0, y0 = src.bounds.left, src.bounds.top
            dx, dy = src.res[0], -src.res[1]

            coords = {'y': np.arange(start=y0, stop=(y0 + ny * dy), step=dy),
                      'x': np.arange(start=x0, stop=(x0 + nx * dx), step=dx)}

            dims = ('y', 'x')

            attrs = {}
            for attr_name in ['crs', 'affine', 'proj']:
                try:
                    attrs[attr_name] = getattr(src, attr_name)
                except AttributeError:
                    pass

    return xr.DataArray(data, dims=dims, coords=coords, attrs=attrs)
