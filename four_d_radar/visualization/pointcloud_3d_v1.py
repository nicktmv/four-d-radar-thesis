import open3d as o3d
import numpy as np


# TODO : Fix paths not being found

def read_bin_file(file_path):
    data = np.fromfile(file_path, dtype=np.float32)
    points = data.reshape(-1, 7)  # Assuming 7 features per point
    return points


def read_label_txt(file_path):
    labels = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split(' ')
            labels.append(parts)
    return labels


def parse_label_info(label):
    # Extract relevant information from the label
    obj_type = label[0]
    dimensions = np.array(list(map(float, label[8:11])))  # h, w, l
    location = np.array(list(map(float, label[11:14])))  # x, y, z
    rotation_y = float(label[14])  # This might need adjustment

    # Adjust the Z-coordinate of the location if it represents the bottom of the bounding box
    location[2] += dimensions[0] / 2  # Assuming the Z-coordinate is the height from ground

    return obj_type, dimensions, location, rotation_y


def rotation_matrix_y(rotation_y):
    # Rotation matrix around the Y-axis (angle in radians)
    return np.array([
        [np.cos(rotation_y), 0, np.sin(rotation_y)],
        [0, 1, 0],
        [-np.sin(rotation_y), 0, np.cos(rotation_y)]
    ])


def visualize_radar_point_cloud(points, labels):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    geometries = [pcd]

    for label in labels:
        obj_type, dimensions, location, rotation_y = parse_label_info(label)

        # Assuming the rotation angle is provided in degrees, convert to radians
        rotation_y_rad = np.radians(rotation_y)

        center = np.array(location).reshape((3, 1))
        extent = np.array(dimensions).reshape((3, 1))
        R = rotation_matrix_y(rotation_y_rad)

        bbox = o3d.geometry.OrientedBoundingBox(center=center, R=R, extent=extent)

        color_map = {'pedestrian': [0, 1, 0], 'cyclist': [0, 0, 1], 'rider': [1, 1, 0]}
        bbox.color = np.array(color_map.get(obj_type.lower(), [1, 0, 0]))

        geometries.append(bbox)

    o3d.visualization.draw_geometries(geometries)


if __name__ == "__main__":
    frame_number = "00544"
    radar_data_path = f'../data/view_of_delft_PUBLIC/view_of_delft_PUBLIC/radar/training/velodyne/{frame_number}.bin'
    label_data_path = f'../data/view_of_delft_PUBLIC/view_of_delft_PUBLIC/lidar/training/label_2/{frame_number}.txt'

    radar_points = read_bin_file(radar_data_path)
    labels = read_label_txt(label_data_path)

    visualize_radar_point_cloud(radar_points, labels)
