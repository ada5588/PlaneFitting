# PlaneFitting
This repository is an implementation for reconstruction 3D scences and compute its metrics mentioned in the paper [A Flexible Technique for Accurate Omnidirectional Camera Calibration and
Structure from Motion](https://ieeexplore.ieee.org/document/1578733). <br>

Knowing points' 3D coodinate, you can use `plane_fitting.py` to compute metrics such as the angle between two planes
and the average distance of points from the fitted plane. `threeD_plot.py` is for plotting points into a 3D graph with the 3D coordinates of points. <br>
`utility.py` contains functions used for computing metrics.

### Before you start, install these packages:
* numpy
* matplotlib

### Get started
Update the path of point data file in `plane_fitting.py` or `threeD_plot.py` and run it. 
*If you want an interactive 3D plot, run `threeD_plot.py` from terminal.*
