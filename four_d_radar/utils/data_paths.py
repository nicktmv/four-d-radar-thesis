"""
A class for storing the paths to the data used in the project.
"""
from pathlib import Path


class DataPaths:
    def _init_(self, root_dir: str):
        self.__root_dir = Path(root_dir)
        self.pointcloud_file_path = 'data/view_of_delft_PUBLIC/radar/training/velodyne'
        self.label_path = 'data/view_of_delft_PUBLIC/lidar/training/label_2'
        self.train_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
        self.test_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/test.txt'
        self.pose_path = 'data/view_of_delft_PUBLIC/lidar/training/pose'
        self.image_path = 'data/view_of_delft_PUBLIC/lidar/training/image_2'
        self.calib_path = 'data/view_of_delft_PUBLIC/lidar/training/calib'

    @property
    def pointcloud_file_path(self):
        return Path(self.__root_dir, self.pointcloud_file_path)

    @property
    def label_path(self):
        return Path(self.__root_dir, self.label_path)

    @property
    def train_indices_path(self):
        return Path(self.__root_dir, self.train_indices_path)

    @property
    def test_indices_path(self):
        return Path(self.__root_dir, self.test_indices_path)

    @property
    def pose_path(self):
        return Path(self.__root_dir, self.pose_path)

    @property
    def image_path(self):
        return Path(self.__root_dir, self.image_path)

    @property
    def calib_path(self):
        return Path(self.__root_dir, self.calib_path)
