import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt


# command line parser
parser = argparse.ArgumentParser(description='Crop boundary to avoid artifacts')
parser.add_argument('obj_name', help='the name of the object')
parser.add_argument('--erode', type=int, default=1, help='how many times you want to erode')

def erode_mask(mask):
    new_mask = np.zeros_like(mask)
    for i in range(1, mask.shape[0]-1):
        for j in range(1, mask.shape[1]-1):
            if mask[i+1,j] and mask[i-1,j] and mask[i,j-1] and mask[i,j+1]:
                new_mask[i, j] = 1
    return new_mask.astype(np.bool_)

if __name__ == '__main__':
    args = parser.parse_args()

    n = np.load("{0}/make_{0}/{0}_normal.npy".format(args.obj_name))
    d = np.load("{0}/make_{0}/{0}_depth.npy".format(args.obj_name))

    mask = d>-9000
    for i in range(args.erode):
        mask = erode_mask(mask)

    for i in range(3):
        n[...,i][~mask] = 0
    d[~mask] = np.nan


    plt.style.use(['science','no-latex'])

    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,4.5))
    axes[0].imshow(n/2+.5)
    axes[0].set_xticks([]), axes[0].set_yticks([]), axes[0].set_title("Normal Map")

    axes[1].imshow(d)
    axes[1].set_xticks([]), axes[1].set_yticks([]), axes[1].set_title("Depth Map")

    plt.show()

    np.save("{0}_gt_depth.npy".format(args.obj_name), d)
    np.save("{0}_normal.npy".format(args.obj_name), n)
