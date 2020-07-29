import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

def substract_offset(d):
    return d-np.nanmean(d)

# command line parser
parser = argparse.ArgumentParser(description='Compare normal integration result by solving Poisson Equation and mesh deformation')
parser.add_argument('gt', help='the path of ground truth normal map')
parser.add_argument('est_p', help='the path of Poisson normal map')
parser.add_argument('est_m', help='the path of mesh deformation normal map')

if __name__ == '__main__':
    args = parser.parse_args()
    gt = np.load(args.gt) # ground truth depth
    est_p = np.load(args.est_p) # estimated depth by poisson
    est_m = np.load(args.est_m) # estimated depth by mesh deformation
    plt.style.use(['science','no-latex'])

    gt = substract_offset(gt)
    est_p = substract_offset(est_p)
    est_m = substract_offset(est_m)
    error_map_p = np.abs(gt-est_p)
    error_map_m = np.abs(gt-est_m)
 
    # fig, axes = plt.subplots(figsize=(4.5,4.5))
    # axes.imshow(error_map)
    # axes.set_title('Error Map')
    # 
    # axes.set_xticks([]), axes.set_yticks([]) # x, y ticks off

    # plt.show()
    
    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,4.5))
    axes[0].imshow(error_map_p)
    axes[0].set_xticks([]), axes[0].set_yticks([]), axes[0].set_title("Poisson Error Map")
    axes[0].set_xlabel('MAE:{:0.2f}'.format(np.nanmean(error_map_p)))
    
    axes[1].imshow(error_map_m)
    axes[1].set_xticks([]), axes[1].set_yticks([]), axes[1].set_title("Mesh Deformation Error Map")
    axes[1].set_xlabel('MAE:{:0.2f}'.format(np.nanmean(error_map_m)))

    plt.show()
