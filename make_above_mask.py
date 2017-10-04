"""Makes a mask for the ABoVE region that's readable by ILAMB."""

import numpy as np
from netCDF4 import Dataset


res = 0.5
latbnd = np.asarray([np.arange(-90, 90, res),
                     np.arange(-90 + res, 90 + 0.01, res)]).T
lonbnd = np.asarray([np.arange(0, 360, res),
                     np.arange(0 + res, 360 + 0.01, res)]).T
lat = latbnd.mean(axis=1)
lon = lonbnd.mean(axis=1)

mask_data = np.loadtxt('data/above_mask.txt', dtype=int)
missing = 0

ids = np.ma.masked_values(mask_data, missing)
lbl = np.asarray(['ABoVE'])

dset = Dataset('ABoVE_mask.nc', mode='w')
dset.createDimension('lat', size=lat.size)
dset.createDimension('lon', size=lon.size)
dset.createDimension('nb', size=2)
dset.createDimension('n', size=lbl.size)

X = dset.createVariable('lat', lat.dtype, ('lat'))
XB = dset.createVariable('lat_bounds', lat.dtype, ('lat','nb'))
Y = dset.createVariable('lon', lon.dtype, ('lon'))
YB = dset.createVariable('lon_bounds',lon.dtype, ('lon','nb'))
I = dset.createVariable('ids',ids.dtype, ('lat','lon'))
L = dset.createVariable('labels',lbl.dtype, ('n'))

X[...] = lat
X.units = 'degrees_north'
XB[...] = latbnd

Y[...] = lon
Y.units = 'degrees_east'
YB[...] = lonbnd

I[...] = ids
I.labels = 'labels'

L[...] = lbl

dset.close()
