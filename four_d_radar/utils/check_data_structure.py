import os
import struct
from pathlib import Path
from four_d_radar.utils.data_paths import DataPaths  # Adjust the import path according to your project structure

NUM_FEATURES = 7
BYTES_PER_FEATURE = 4
DATA_POINT_SIZE = NUM_FEATURES * BYTES_PER_FEATURE
NUM_POINTS_TO_CHECK = 5


def check_point_cloud_file(file_path: Path):
    """
    Reads and checks a point cloud file's structure by validating the size of the data points.

    Parameters:
    file_path (Path): The Path object pointing to the point cloud file to be checked.

    This function prints out the total size of the data, the calculated number of points based on the assumed size of
    each point, and the remainder of this calculation (which should ideally be 0, to prove that NUM_FEATURES = 7 and
    BYTES_PER_FEATURE = 4). It also prints out the data points for the first NUM_POINTS_TO_CHECK  as a sanity check.
    """
    # Ensure the file exists
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    try:
        with open(file_path, 'rb') as file:
            data = file.read()  # Read the entire file

        # Calculate the number of points and the remainder
        num_points = len(data) // DATA_POINT_SIZE
        remainder = len(data) % DATA_POINT_SIZE

        # Print results
        print(f"Total data length in bytes: {len(data)}")
        print(f"Number of points calculated: {num_points}")
        print(f"Remainder = {remainder} (should be 0 if assumption is correct)")

        # Check a few points to see if the assumption holds
        for i in range(min(num_points, NUM_POINTS_TO_CHECK)):
            point_data = data[i * DATA_POINT_SIZE:(i + 1) * DATA_POINT_SIZE]  # Extract the data for one point
            point = struct.unpack(f'{NUM_FEATURES}f', point_data)  # Unpack the point data
            print(f"Point {i + 1}: {point}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to check the structure of a specific point cloud file using the DataPaths class.
    """
    # Initialize the DataPaths class with your root directory
    root_dir = "D:/four-d-radar-thesis"
    data_paths = DataPaths(root_dir)

    # Specifying the file to check relative to the point cloud directory
    relative_file_path = '00770.bin'
    full_file_path = data_paths.point_cloud_file_path / relative_file_path

    # Check the point cloud file
    check_point_cloud_file(full_file_path)


if __name__ == "__main__":
    main()
