import open3d as o3d
import numpy as np
import json

"""This visualization script reads a binary file containing radar point cloud data and a JSON file containing labels 
for the bounding boxes of objects in the radar data. It then visualizes the radar point cloud in 3D using Open3D, 
with the radar origin, coordinate axes, and bounding box lines for each object."""


def read_bin_file(file_path):
    # Read binary file containing radar point cloud
    data = np.fromfile(file_path, dtype=np.float32)
    # Reshape the array to Nx7
    points = data.reshape(-1, 7)
    return points


def read_label_json(file_path):
    with open(file_path, 'r') as json_file:
        labels = json.load(json_file)
    return labels


def visualize_radar_point_cloud(points, labels):
    # Create Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])  # Extract x, y, z columns

    # Create a sphere to represent radar origin
    radar_origin = o3d.geometry.TriangleMesh.create_sphere(radius=0.5)
    radar_origin.paint_uniform_color([1, 0, 0])  # Set color to red

    # Create coordinate axes lines
    axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)

    # Add point cloud, radar origin, and axes to the same visualization
    geometries = [pcd, radar_origin, axes]

    # Add bounding box lines to the visualization
    for label in labels:
        if 'geometry' in label and 'center' in label['geometry'] and 'size' in label['geometry']:
            center = label['geometry']['center']
            size = label['geometry']['size']
            quaternion = label['geometry']['quaternion']

            # Calculate corner points of the bounding box
            corners = np.array([
                [-size['width'] / 2, -size['height'] / 2, -size['length'] / 2],
                [size['width'] / 2, -size['height'] / 2, -size['length'] / 2],
                [size['width'] / 2, size['height'] / 2, -size['length'] / 2],
                [-size['width'] / 2, size['height'] / 2, -size['length'] / 2],
                [-size['width'] / 2, -size['height'] / 2, size['length'] / 2],
                [size['width'] / 2, -size['height'] / 2, size['length'] / 2],
                [size['width'] / 2, size['height'] / 2, size['length'] / 2],
                [-size['width'] / 2, size['height'] / 2, size['length'] / 2]
            ])

            # Rotate and translate the corners based on quaternion and center
            rotation_matrix = o3d.geometry.get_rotation_matrix_from_quaternion(
                (quaternion['w'], quaternion['x'], quaternion['y'], quaternion['z']))
            corners = np.dot(corners, rotation_matrix.T) + np.array([center['x'], center['y'], center['z']])

            # Define lines for bounding box edges
            lines = [
                (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom rectangle
                (4, 5), (5, 6), (6, 7), (7, 4),  # Top rectangle
                (0, 4), (1, 5), (2, 6), (3, 7)  # Connecting lines
            ]

            # Create LineSet for bounding box edges
            line_set = o3d.geometry.LineSet(
                points=o3d.utility.Vector3dVector(corners),
                lines=o3d.utility.Vector2iVector(lines)
            )

            # Set color based on the class name
            if label['className'] == 'pedestrian':
                line_set.paint_uniform_color([0, 0, 1])  # Blue for pedestrians
            elif label['className'] == 'bicycle':
                line_set.paint_uniform_color([0, 1, 0])  # Green for cyclists
            else:
                line_set.paint_uniform_color([1, 0, 0])  # Red for other objects

            # Add LineSet to geometries
            geometries.append(line_set)

    o3d.visualization.draw_geometries(geometries)


if __name__ == "__main__":
    # Replace 'path_to_your_file.bin' and 'path_to_your_label.json' with the actual paths
    file_path = '../../data/example_set/radar/training/velodyne/01047.bin'
    label_path = '../../data/example_set/radar/training/label_2/01047.json'

    # Read radar point cloud from binary file
    radar_points = read_bin_file(file_path)

    # Read labels from JSON file
    labels = read_label_json(label_path)

    # Visualize radar point cloud with radar origin, coordinate axes, and bounding box lines
    visualize_radar_point_cloud(radar_points, labels)
