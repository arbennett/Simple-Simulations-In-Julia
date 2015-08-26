#
# Draw images for the wave_eq.jl solutions
#

import os

import numpy as np
import matplotlib.colorbar as colorbar
import matplotlib.pyplot as plt

data_dir = "out"
data_files = sorted(os.listdir(data_dir))

for data in data_files:
    fig, ax = plt.subplots()
    vals = np.genfromtxt(data_dir + os.sep + data) 
    cax = ax.imshow(vals)
    fig.colorbar(cax)
    plt.savefig("imgs" + os.sep + data + ".png")
    plt.close()

