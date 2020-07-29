import OpenEXR
import Imath
import sys
import scipy.io as io
import numpy as np
import cv2
from matplotlib import pyplot as plt


def split_channel(f, channel, float_flag=True):
    dw = f.header()['dataWindow']
    size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    if float_flag:
        pt = Imath.PixelType(Imath.PixelType.FLOAT)
    else:
        pt = Imath.PixelType(Imath.PixelType.HALF)
    channel_str = f.channel(channel, pt)
    img = np.frombuffer(channel_str, dtype=np.float32)
    img.shape = (size[1], size[0])
    return img


def main(exr_name, output_name, output_format):
    f = OpenEXR.InputFile(exr_name)

    channels = dict()
    for channel_name in f.header()["channels"]:
        print(channel_name)
        split_channel(f, channel_name)
        channels[channel_name] = split_channel(f, channel_name)

    normal = np.concatenate((channels["normal.R"][:, :, None], channels["normal.G"][:, :, None], channels["normal.B"][:, :, None]), axis=-1)
    depth = np.array(channels["depth.B"])
    
    if output_format == "npy":
        np.save("{0}_normal.npy".format(output_name), normal)
        np.save("{0}_depth.npy".format(output_name), depth)
    else:
        io.savemat('{0}_normal.mat'.format(output_name), {'est_normal': normal})
        io.savemat('{0}_depth.mat'.format(output_name), {'est_depth': depth})

    fig1 = plt.subplot(1, 2, 1)
    fig1 = plt.imshow(normal/2+.5)
    fig1.axes.get_xaxis().set_visible(False)
    fig1.axes.get_yaxis().set_visible(False)

    fig2 = plt.subplot(1, 2, 2)
    fig2 = plt.imshow(depth, "gray")
    fig2.axes.get_xaxis().set_visible(False)
    fig2.axes.get_yaxis().set_visible(False)

    plt.show()


if  __name__ =="__main__":
    if sys.argv[1] == "--help":
        print("usage: python exr-read.py input-exr outputname npy(or mat)")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
