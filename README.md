# graph-reader
Converting report and paper graphs to data

Version: 1.0
Date: February 2021
Author: Louis Kokee
Description: graph reader v1 takes as input screenshots of normal plots (not log-log or semilog plots) from reports or papers. Running the main opens the plot, after which the user has to set a selection of points. The first couple of points that are set are to define the bases and origins of the vertical and horizontal axis of the profile that will be read. The points that are set after these make up the profile. These latter points should, for high accuracy, (1) populate the profile densely in regions of large curvature, (2) be placed at the center of the profile and (3) make up a strictly forwards or strictly backwards path along the profile.

INPUTS: 
image_path = 'source_figures/xxx.png'     
profile_name = 'xxx'                      - the output data will be named "xxx.npz" in ./output_data
verAxis_base = 100                        - the size of the user-set vertical axis base (in the units shown in the source graph)
horAxis_base = 100                        - the size of the user-set horizontal axis base (in the units shown in the source graph)

# setting the points
A point are set by (1) moving the cursor over the right position, (2) clicking the left mouse button to select the point and (3) clicking "s" on the keyboard to confirm the point. The points are set in the following order:
Point nr.     Name.                         
1             Vertical axis base start      
2             Vertical axis base end
3             Vertical axis origin
4             Horizontal axis base start
5             Horizontal axis base end
6             Horizontal axis base origin
7, 8, 9, ...  Points that define the graph to be read

# known issues and limitations
Accurately setting points in the middle of the profile is difficult for two reasons. Firstly, the points can only be set at discreet pixel locations. Sometimes, the profile center is somewhere in between two pixels. Secondly, there is no zoom functionality, so moving around the mouse to accurately select the right pixel is difficult. 

There is no on-screen feedback showing where points have been set already. So it is not entirely clear if the points have been set with sufficient density. Furthermore, without this feedback, it is possible to accidentally set points that do not strictly travel forwards on the profile. 
