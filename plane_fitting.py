import pickle
import numpy as np
import utility

# Load points' 3-dimensional coordinates
# I use a pickle file to store points data this time
file_name = 'point_coordinate_data_file_path'
with open(file_name, 'rb') as fp:
    points = pickle.load(fp)

# Make sure the coordinates is saved in an array with
# a shape of (n, 3). n is the number of points
points = np.asarray(points)

# Get the normal vector of the plane best fitting the points
normal_v = utility.normal_vector(points)

# Get the average distance between points and the best fitting plane
avg_distance = utility.avg_distance_point2plane(points)

# With two normal vectors of planes, we can calculate the angle between those planes
# I use ex_normal_v1 and ex_normal_v2 for example. They are the normal vectors of ex_plane1 and ex_plane2.
ex_normal_v1 = np.asarray([0, 1, 1])
ex_normal_v2 = np.asarray([0, 0, 1])
print('angle between ex_plane1 and ex_plane2:',
      180 - utility.angle(ex_normal_v1, ex_normal_v2))
