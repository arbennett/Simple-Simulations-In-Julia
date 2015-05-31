#
# Draw images for the wave_eq.jl solutions
#

import os

import numpy as np
import matplotlib.pyplot as plt

data_dir = "out"
data_files = sorted(os.listdir(data_dir))

for data in data_files:
    vals = np.genfromtxt(data_dir + os.sep + data) 
    plt.imshow(vals, vmin=0, vmax=2)
    plt.savefig("imgs" + os.sep + data + ".png")

