import pickle
import matplotlib.pyplot as plt
import numpy as np

plane_points_1 = 'point_coordinate_data_file_path'
plane_points_2 = 'point_coordinate_data_file_path'
plane_points_3 = 'point_coordinate_data_file_path'

with open(plane_points_1, 'rb') as fp:
    plane_1 = pickle.load(fp)

with open(plane_points_2, 'rb') as fp:
    plane_2 = pickle.load(fp)

with open(plane_points_3, 'rb') as fp:
    plane_3 = pickle.load(fp)

plane_1 = np.asarray(plane_1)
plane_2 = np.asarray(plane_2)
plane_3 = np.asarray(plane_3)

plt.figure()
ax = plt.subplot(111, projection='3d')
ax.scatter(plane_1[:, 0], plane_1[:, 1], plane_1[:, 2], color='b')
ax.scatter(plane_2[:, 0], plane_2[:, 1], plane_2[:, 2], color='g')
ax.scatter(plane_3[:, 0], plane_3[:, 1], plane_3[:, 2], color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()