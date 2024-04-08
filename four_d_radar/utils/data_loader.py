import os
import numpy as np
import struct
from four_d_radar.utils.data_paths import DataPaths

NUM_FEATURES = 7
BYTES_PER_FEATURE = 4
DATA_POINT_SIZE = NUM_FEATURES * BYTES_PER_FEATURE


def load_indices(indices_path):
    """
    Load a list of indices from ImageSets/train.txt and test.txt.

    Parameters:
    indices_path (str): The file path containing the indices.

    Returns:
    list[str]: A list of indices, each stripped of leading/trailing whitespace.
    """
    with open(indices_path, 'r') as file:
        return [line.strip() for line in file]


def load_labels(label_path, frame_number):
    """
    Load labels from lidar/training/label_2/specified file corresponding to a .bin frame number, if it exists.

    Parameters:
    label_path (str): The directory path where label files are stored.
    frame_number (str): The frame number corresponding to the label file.

    Returns: list[list[str]]: A list of labels, where each label is a list of string elements parsed from a single
    line in the label file.
    """
    label_file_path = os.path.join(label_path, frame_number.replace('.bin', '.txt'))
    labels = []

    if os.path.exists(label_file_path):
        with open(label_file_path, 'r') as file:
            labels = [line.strip().split(' ') for line in file]
        print(f"Loaded {len(labels)} labels for {frame_number}")
    else:
        print(f"Label file {label_file_path} not found.")
    return labels


def load_binary_data(file_path):
    """
    Reads binary point cloud data from a specified file.

    Parameters:
    file_path (str): The file path to read the binary data from.

    Returns:
    bytes: The raw binary data read from the file.
    """
    with open(file_path, 'rb') as file:
        return file.read()


def unpack_data(pointcloud, num_points):
    """
    Unpack binary raw point cloud data into a structured numpy array.

    Parameters:
    pointcloud (bytes): The raw binary point cloud data.
    num_points (int): The number of points to be unpacked from the pointcloud data.

    Returns:
    np.ndarray: A numpy array containing the unpacked point cloud data, or None if an error occurs during unpacking.
    """
    try:
        points = np.array(struct.unpack(f'{num_points * NUM_FEATURES}f', pointcloud)).reshape(
            (num_points, NUM_FEATURES))
        return points
    except struct.error as e:
        print(f"Error unpacking data: {e}")
        return None


def load_data_and_labels(pointcloud_file_path, label_path, frame_number, load_labels_flag):
    """
    Loads point cloud data and optionally labels for a given frame.

    Parameters:
    pointcloud_file_path (str): The directory path where point cloud data files are stored.
    label_path (str): The directory path where label files are stored.
    frame_number (str): The frame number to load the binary data and labels for.
    load_labels_flag (bool): A flag indicating whether to load labels along with the data.

    Returns: tuple: A tuple containing two lists, the first is a list of numpy arrays of point cloud data,
    and the second is a list of labels (empty if load_labels_flag is False).
    """
    file_path = os.path.join(pointcloud_file_path, frame_number)
    pointcloud = load_binary_data(file_path)
    num_points = len(pointcloud) // DATA_POINT_SIZE

    pointcloud_point_list, labels_list = [], []

    if num_points > 0:
        points = unpack_data(pointcloud, num_points)
        if points is not None:
            pointcloud_point_list.append(points)
            if load_labels_flag:
                labels = load_labels(label_path, frame_number)
                labels_list.append(labels)
    else:
        print(f"No points found in {frame_number}.")

    return pointcloud_point_list, labels_list


def load_data_from_files(pointcloud_file_path, label_path, files, load_labels_flag):
    """
    Loads point cloud data and optionally labels from a list of frame numbers.

    Parameters:
    pointcloud_file_path (str): The directory path where point cloud data files are stored.
    label_path (str): The directory path where label files are stored.
    files (list[str]): A list of frame numbers to load data and labels for.
    load_labels_flag (bool): A flag indicating whether to load labels along with the data.

    Returns: tuple: A tuple containing two lists, the first is a list of numpy arrays of point cloud data,
    and the second is a list of labels (empty if load_labels_flag is False).
    """
    data_list, labels_list = [], []
    labels_loaded_count = 0

    for frame_number in files:
        data, labels = load_data_and_labels(pointcloud_file_path, label_path, frame_number, load_labels_flag)
        if data:
            data_list.extend(data)
            if labels:
                labels_list.extend(labels)
                labels_loaded_count += 1

    if load_labels_flag:
        print(f"Successfully loaded {labels_loaded_count} labels for {len(files)} .bin files.")

    return data_list, labels_list if load_labels_flag else data_list


def load_dataset(pointcloud_file_path, label_path, indices_path, load_labels_flag=True):
    """
    Loads a dataset based on indices and specified paths, including point cloud data and optionally labels.

    Parameters:
    pointcloud_file_path (str): The directory path where point cloud data files are stored.
    label_path (str): The directory path where label files are stored.
    indices_path (str): The file path containing the indices of frames to load.
    load_labels_flag (bool): A flag indicating whether to load labels along with the data.

    Returns: tuple: A tuple containing two lists, the first is a list of numpy arrays of point cloud data,
    and the second is a list of labels (empty if load_labels_flag is False).
    """
    if not os.path.exists(pointcloud_file_path):
        print(f"Directory {pointcloud_file_path} does not exist.")
        return [], []

    indices = load_indices(indices_path)
    file_list = [f"{idx}.bin" for idx in indices if os.path.exists(os.path.join(pointcloud_file_path, f"{idx}.bin"))]

    return load_data_from_files(pointcloud_file_path, label_path, file_list, load_labels_flag)


def run_data_loader(root_dir):
    data_paths = DataPaths(root_dir)

    print("Loading training data...")
    train_data, train_labels = load_dataset(data_paths, data_paths.train_indices_file_path, load_labels_flag=True)
    if train_data:
        print(f"Number of points in the first training file: {len(train_data[0])}")

    print("\nLoading testing data...")
    test_data, _ = load_dataset(data_paths, data_paths.test_indices_file_path, load_labels_flag=False)
    if test_data:
        print("Successfully loaded test data")
        print(f"Number of points in the first testing file: {len(test_data[0])}")


if __name__ == "__main__":
    root_dir = "Your root directory here"
    run_data_loader(root_dir)
