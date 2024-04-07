import open3d as o3d
import numpy as np

from four_d_radar.utils.data_loader import load_dataset


def read_label_file(file_path):
    labels = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            # Extract label information assuming the format provided in your example
            obj_type, truncation, occlusion, alpha, bbox_2d, dimensions, location, rotation_y = parts[0], float(
                parts[1]), int(parts[2]), float(parts[3]), np.array(parts[4:8], dtype=float), np.array(parts[8:11],
                                                                                                       dtype=float), np.array(
                parts[11:14], dtype=float), float(parts[14])
            labels.append((obj_type, truncation, occlusion, alpha, bbox_2d, dimensions, location, rotation_y))
    return labels


def visualize_radar_point_cloud(points, labels):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])

    radar_origin = o3d.geometry.TriangleMesh.create_sphere(radius=0.5)
    radar_origin.paint_uniform_color([1, 0, 0])

    axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)

    geometries = [pcd, radar_origin, axes]

    for label in labels:
        obj_type, truncation, occlusion, alpha, bbox_2d, dimensions, location, rotation_y = label
        bbox = o3d.geometry.OrientedBoundingBox(location, np.eye(3), dimensions)
        bbox.rotate(bbox.get_rotation_matrix_from_yaw(rotation_y), center=bbox.center)

        # Customize color based on object type
        if obj_type == "Pedestrian":
            bbox.color = np.array([0, 1, 0])  # Green
        elif obj_type == "Cyclist":
            bbox.color = np.array([0, 0, 1])  # Blue
        else:
            bbox.color = np.array([1, 0, 0])  # Red for others

        geometries.append(bbox)

    o3d.visualization.draw_geometries(geometries)


def visualize_frame(frame_number, data_path, label_path):
    frame_data, frame_labels = load_dataset(data_path, label_path, f"{frame_number}.txt")

    if frame_data and frame_labels:
        print(f"Visualizing frame {frame_number}...")
        visualize_radar_point_cloud(frame_data[0], frame_labels[0])
    else:
        print(f"Failed to load data for frame {frame_number}.")


# Example usage
frame_number = "00544"
data_path = '../../data/view_of_delft_PUBLIC/radar/training/velodyne'
label_path = '../../data/view_of_delft_PUBLIC/lidar/training/label_2'

visualize_frame(frame_number, data_path, label_path)
