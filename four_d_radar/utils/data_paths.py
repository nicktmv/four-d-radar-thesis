from pathlib import Path


class DataPaths:
    def __init__(self, root_dir: str):
        self.__root_dir = Path(root_dir)
        self._pointcloud_path = 'data/view_of_delft_PUBLIC/radar/training/velodyne'
        self._label_path = 'data/view_of_delft_PUBLIC/lidar/training/label_2'
        self._indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets'  # not sure if needed
        self._train_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
        self._test_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/test.txt'
        self._pose_path = 'data/view_of_delft_PUBLIC/lidar/training/pose'
        self._image_path = 'data/view_of_delft_PUBLIC/lidar/training/image_2'
        self._calib_path = 'data/view_of_delft_PUBLIC/lidar/training/calib'

    @property
    def pointcloud_file_path(self):
        return self.__root_dir / self._pointcloud_path

    @property
    def label_file_path(self):
        return self.__root_dir / self._label_path

    @property
    def indices_file_path(self):
        return self.__root_dir / self._indices_path

    @property
    def train_indices_file_path(self):
        return self.__root_dir / self._train_indices_path

    @property
    def test_indices_file_path(self):
        return self.__root_dir / self._test_indices_path

    @property
    def pose_file_path(self):
        return self.__root_dir / self._pose_path

    @property
    def image_file_path(self):
        return self.__root_dir / self._image_path

    @property
    def calib_file_path(self):
        return self.__root_dir / self._calib_path
