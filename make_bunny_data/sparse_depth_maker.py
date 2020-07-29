import numpy as np
from matplotlib import pyplot as plt

# n = np.load("bunny_normal.npy")
d = np.load("bunny_depth.npy")
# d = np.load("bunny_sparse_depth.npy")


mask = np.abs(d)<=100

mask[:,:] = np.False_
mask[41:56,74:86] = np.True_
mask[49:59,124:155] = np.True_
mask[111:128,55:74] = np.True_
mask[165:196,77:106] = np.True_
mask[185:211,183:206] = np.True_
mask[246:259,110:124] = np.True_
mask[220:232,262:276] = np.True_
mask[218:234,124:138] = np.True_


d[~mask] = np.nan

plt.figure()
plt.imshow(d, "gray")
plt.show()

np.save("bunny_sparse_depth", d)

# mask = np.abs(n[...,2])<=0.09

# n[...,0][mask] = 0
# n[...,1][mask] = 0
# n[...,2][mask] = 0

# plt.figure()
# plt.imshow(n/2+.5)
# plt.show()

# np.save("bunny_normal", n)