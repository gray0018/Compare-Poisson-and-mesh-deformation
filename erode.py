
import numpy as np
import matplotlib.pyplot as plt


def erode_mask(mask):
    new_mask = np.zeros_like(mask)
    for i in range(1, mask.shape[0]-1):
        for j in range(1, mask.shape[1]-1):
            if mask[i+1,j] and mask[i-1,j] and mask[i,j-1] and mask[i,j+1]:
                new_mask[i, j] = 1
    return new_mask.astype(np.bool_)

n = np.load("dragon_normal.npy")
d = np.load("dragon_depth.npy")

mask = d>-1000
for i in range(3):
    mask = erode_mask(mask)

for i in range(3):
    n[...,i][~mask] = 0
d[~mask] = np.nan


np.save("dragon_depth.npy", d)
np.save("dragon_normal.npy", n)
