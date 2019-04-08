import scipy.io
import pandas as pd
import h5py

# mat = h5py.File('attributesGroundtruth-1-0.mat')
# mat = {k:v for k, v in mat.items() if k[0] != '_'}
# data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.iteritems()})
# data.to_csv("attributesGroundtruth-1-0.csv")


import scipy.io
f = h5py.File('attributesGroundtruth-1-0.mat')

print(list(f.keys()))

dset = f['annos']


print(dset)