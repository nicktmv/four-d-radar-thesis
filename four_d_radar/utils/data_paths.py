from pathlib import Path


class DataPaths:
    def __init__(self, root_dir: str):
        self.__root_dir = Path(root_dir)
        self._pointcloud_rel_path = 'data/view_of_delft_PUBLIC/radar/training/velodyne'
        self._label_rel_path = 'data/view_of_delft_PUBLIC/lidar/training/label_2'
        self._train_indices_rel_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
        self._test_indices_rel_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/test.txt'
        self._pose_rel_path = 'data/view_of_delft_PUBLIC/lidar/training/pose'
        self._image_rel_path = 'data/view_of_delft_PUBLIC/lidar/training/image_2'
        self._calib_rel_path = 'data/view_of_delft_PUBLIC/lidar/training/calib'

    @property
    def pointcloud_file_path(self):
        return self.__root_dir / self._pointcloud_rel_path

    @property
    def label_path(self):
        return self.__root_dir / self._label_rel_path

    @property
    def train_indices_path(self):
        return self.__root_dir / self._train_indices_rel_path

    @property
    def test_indices_path(self):
        return self.__root_dir / self._test_indices_rel_path

    @property
    def pose_path(self):
        return self.__root_dir / self._pose_rel_path

    @property
    def image_path(self):
        return self.__root_dir / self._image_rel_path

    @property
    def calib_path(self):
        return self.__root_dir / self._calib_rel_path
