"""
A class for storing the paths to the data used in the project.
"""


class DataPaths:
    def __init__(self):
        self.data_path = '../../data/view_of_delft_PUBLIC/radar/training/velodyne'
        self.label_path = '../../data/view_of_delft_PUBLIC/lidar/training/label_2'
        self.train_indices_path = '../../data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
        self.test_indices_path = '../../data/view_of_delft_PUBLIC/lidar/ImageSets/test.txt'
        self.pose_path = '../../data/view_of_delft_PUBLIC/lidar/training/pose'
        self.image_path = '../../data/view_of_delft_PUBLIC/lidar/training/image_2'
        self.calib_path = '../../data/view_of_delft_PUBLIC/lidar/training/calib'
