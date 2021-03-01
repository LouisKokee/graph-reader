# header
# This script takes a
#
# modules
import numpy as np
from functions import *


# --- USER INPUT ---
saveData = 1
printData = 1
image_path = 'source_figures/xaPre_height_mvw.png'
profile_name = 'xaPre_height_mvw_stable'
verAxis_base = 500
horAxis_base = 0.12


# --- OPEN GUI AND SET POINTS ---
# read coordinates (user input)
IX, IY = set_graph_coordinates(image_path)


# --- TRANSFORM DATA FROM LIST OF PIXELS TO DATA IN GRAPH UNITS ---
# amount of pixels base takes up
verAxis_base_pixels = -(IY[1]-IY[0])
horAxis_base_pixels = IX[4]-IX[3]

# data in pixel units
verAxis_pixList = -(IY[6:]-IY[2])
horAxis_pixList = IX[6:]-IX[5]

# convert pixels to graph units
y = pixList_to_graphData(verAxis_pixList, verAxis_base, verAxis_base_pixels)
x = pixList_to_graphData(horAxis_pixList, horAxis_base, horAxis_base_pixels)


# --- SAVE DATA ---
if saveData: np.savez(fr'output_data/{profile_name}',y=y,x=x)
if printData: print(x,y)



