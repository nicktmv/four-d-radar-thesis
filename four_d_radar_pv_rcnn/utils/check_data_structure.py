import os
import struct

"""
This script is designed to verify an assumption made in the data_loader.py file regarding the structure of binary 
data files. Specifically, it addresses the assumption made at line 33 of data_loader.py, where the number of points 
in a binary file is calculated as the total length of the file divided by 28, based on the presumption that each data 
point consists of 7 features, each feature being 4 bytes in size. The script validates this assumption by reading a 
sample binary file, calculating the number of data points based on the aforementioned assumption, and checking if the 
file length is fully divisible by 28 with no remainder. Additionally, it unpacks and prints the first few data points 
(or less, depending on the total number of points) to provide a quick sanity check of the values, further aiding in 
the validation of the data structure assumption.
"""


def main():
    file_path = '../../data/view_of_delft_PUBLIC/radar/training/velodyne/00544.bin'

    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        with open(file_path, 'rb') as file:
            data = file.read()  # Read the entire file
        # Calculate the number of points assuming each point is represented by 28 bytes (7 features x 4 bytes each)
        num_points = len(data) // 28
        remainder = len(data) % 28
        # Print results
        print(f"Total data length in bytes: {len(data)}")
        print(f"Number of points calculated: {num_points}")
        print(f"Remainder (should be 0 if assumption is correct): {remainder}")

        # Check a few points to see if the assumption holds
        for i in range(min(num_points, 5)):  # Check the first 5 points or the total number of points if less than 5
            point_data = data[i * 28:(i + 1) * 28]  # Extract the data for one point
            point = struct.unpack('7f', point_data)  # Unpack the point data
            print(f"Point {i + 1}: {point}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
