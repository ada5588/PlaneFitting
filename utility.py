import numpy as np


def normal_vector(point_array: np.ndarray) -> np.ndarray:
    """Get the normal vector of the best fitting plane."""
    point_array = point_array.T
    # Subtract the centroid and do SVD
    svd = np.linalg.svd(point_array - np.mean(point_array, axis=1, keepdims=True))
    # Extract the left singular vectors
    left = svd[0]
    # the corresponding left singular vector is the normal vector of the best-fitting plane
    normal_vec = left[:, -1]
    return normal_vec


def avg_distance_point2plane(point_array: np.ndarray) -> float:
    """Calculate the average distance between points and the best fitting plane. """
    normal_vec = normal_vector(point_array)
    centroid = np.mean(point_array, axis=0).T
    d = np.dot(centroid, normal_vec)
    sum_distance = 0
    for i in point_array:
        sum_distance += abs(np.dot(i, normal_vec) - d)
    return sum_distance/point_array.shape[0]


def angle(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate the angle between two vectors in degree"""
    angle_rad = np.arccos(np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    return np.rad2deg(angle_rad)


