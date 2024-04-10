import numpy as np
from vod.configuration import KittiLocations

Kitt_locations = KittiLocations()


def homogeneous_coordinates(points):
    if points.shape[1] != 3:
        raise ValueError(f"Expected point dimension to be Nx3, got {points.shape[1]} instead")
    return np.hstack((points, np.ones((points.shape[0], 1), dtype=points.dtype)))


def apply_transformation(points, transformation_matrix):
    if transformation_matrix.shape != (4, 4):
        raise ValueError(f"Expected transformation matrix shape to be 4x4, got {transformation_matrix.shape} instead")
    if points.shape[1] != 4:
        raise ValueError(
            f"Expected point dimension in homogeneous coordinates to be Nx4, got {points.shape[1]} instead")
    return np.dot(transformation_matrix, points.T).T[:, :3]  # Convert back to non-homogeneous coordinates


def transform_point_cloud(point_cloud, transformation_matrix):
    # Convert to homogeneous coordinates
    homo_points = homogeneous_coordinates(
        point_cloud[:, :3])  # Assuming the point cloud is in the format [x, y, z, ...]
    # Apply transformation
    transformed_points = apply_transformation(homo_points, transformation_matrix)
    return transformed_points


def main():
    # Example point cloud data (5 points)
    point_cloud = np.array([
        [0, 0, 0],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    # Transformation matrix to shift points by 1 along the x-axis
    transformation_matrix = np.array([
        [1, 0, 0, 1],  # Add 1 to the x coordinate
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # Apply the transformation to the example point cloud
    transformed_point_cloud = transform_point_cloud(point_cloud, transformation_matrix)

    print("Original Point Cloud:")
    print(point_cloud)
    print("\nTransformed Point Cloud:")
    print(transformed_point_cloud)


if __name__ == "__main__":
    main()
