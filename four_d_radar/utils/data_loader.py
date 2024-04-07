import os
import struct
import numpy as np

from four_d_radar.utils.paths import Paths

"""
This script is designed to load and process 3D point cloud data and associated labels from the VOD dataset. It 
is structured into several key functions to facilitate this process:

1. `load_indices(indices_path)`: Reads a file containing indices (identifiers for data points or sets) and 
returns a list of these indices. This function is useful for segregating the dataset into training, validation, 
and testing sets.

2. `load_labels(label_path, file_name)`: For a given binary data file, this function finds and loads the 
corresponding label file, which shares the same base filename but a different extension (.txt instead of .bin). It 
reads the label file line by line, splitting each line into a list of labels, and returns a list of these label 
lists. If the label file does not exist, it prints a warning.

3. `load_data_from_files(data_path, label_path, files, load_labels_flag=True)`: Iterates over file names to load 
binary point cloud data, converting each point's 7 features (4 bytes each) into a numpy array. If `load_labels_flag` 
is True, corresponding labels are loaded. Returns point cloud data as numpy arrays and, optionally, labels as lists.

4. `load_dataset(data_path, label_path, indices_path, load_labels_flag=True)`: Prepares and loads the dataset by 
verifying the data directory's existence, reading file indices, and constructing file names to load point cloud data 
and, optionally, labels via `load_data_from_files`. Returns the loaded data and labels.

The script includes an example usage section that demonstrates how to load both training and testing datasets from 
specified paths. It distinguishes between training and testing data by using the `load_labels_flag` parameter to 
control whether labels should be loaded (true for training data, false for testing data, since the test data does not 
have associated labels).
"""


def load_indices(indices_path):
    with open(indices_path, 'r') as file:
        indices = [line.strip() for line in file]
    return indices


def load_labels(label_path, file_name):
    label_file_path = os.path.join(label_path, file_name.replace('.bin', '.txt'))
    labels = []
    if os.path.exists(label_file_path):
        with open(label_file_path, 'r') as file:
            for line in file:
                # datawrapper = DataWrapper(line.strip().split(' '))
                labels.append(line.strip().split(' '))
        print(f"Loaded {len(labels)} labels for {file_name}")  # Print number of labels loaded for each file
    else:
        print(f"Label file {label_file_path} not found.")
    return labels


#
# class DataWrapper:
#     def __int__(self, data_list: list):
#         self._data_list = data_list
#
#     def get_category(self):
#         self._data_list[0]


def load_data_from_files(data_path, label_path, files, load_labels_flag=True):
    data_list = []
    labels_list = []
    labels_loaded_count = 0  # Initialize counter for files with labels loaded
    for file_name in files:
        file_path = os.path.join(data_path, file_name)
        with open(file_path, 'rb') as f:
            data = f.read()
            # datawrapper
            num_points = len(data) // 28  # Assuming 7 features x 4 bytes each
            if num_points > 0:
                try:
                    points = np.array(struct.unpack(f'{num_points * 7}f', data)).reshape((num_points, 7))
                    data_list.append(points)
                    if load_labels_flag:
                        labels = load_labels(label_path, file_name)
                        labels_list.append(labels)
                        if labels:  # Check if any labels were loaded
                            labels_loaded_count += 1
                except struct.error as e:
                    print(f"Error unpacking {file_name}: {e}")
            else:
                print(f"No points found in {file_name}.")
    if load_labels_flag:
        print(f"Labels were loaded for {labels_loaded_count} out of {len(files)} files.")  # Summary of labels loaded
    return data_list, labels_list if load_labels_flag else data_list


def load_dataset(data_path, label_path, indices_path, load_labels_flag=True):
    if not os.path.exists(data_path):
        print(f"Directory {data_path} does not exist.")
        return [], []

    indices = load_indices(indices_path)

    file_list = [f"{idx}.bin" for idx in indices if os.path.exists(os.path.join(data_path, f"{idx}.bin"))]

    return load_data_from_files(data_path, label_path, file_list, load_labels_flag)


def main():
    # Instantiate the Paths class to get directory paths
    paths = Paths()

    print("Loading training data...")
    train_data, train_labels = load_dataset(paths.data_path, paths.label_path, paths.train_indices_path,
                                            load_labels_flag=True)
    if train_data:
        print(f"Number of points in the first training file: {len(train_data[0])}")

    print("\nLoading testing data...")
    test_data, test_labels = load_dataset(paths.data_path, paths.label_path, paths.test_indices_path,
                                          load_labels_flag=False)
    if test_data:
        print(f"Number of points in the first testing file: {len(test_data[0])}")


if __name__ == "__main__":
    main()
