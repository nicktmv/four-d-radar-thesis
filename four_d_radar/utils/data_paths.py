from pathlib import Path


class DataPaths:
    """
    A class to manage and provide easy access to various data file paths used within the project.
    """
    def __init__(self, root_dir: str):
        """
        Initializes the DataPaths object with paths to various components of the dataset.

        Parameters:
            root_dir (str): The root directory where the dataset is located.
        """
        self.__root_dir = Path(root_dir)
        self._point_cloud_path = 'data/view_of_delft_PUBLIC/radar/training/velodyne'
        self._label_path = 'data/view_of_delft_PUBLIC/lidar/training/label_2'
        self._indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets'
        self._train_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
        self._test_indices_path = 'data/view_of_delft_PUBLIC/lidar/ImageSets/test.txt'
        self._pose_path = 'data/view_of_delft_PUBLIC/lidar/training/pose'
        self._image_path = 'data/view_of_delft_PUBLIC/lidar/training/image_2'
        self._calib_path = 'data/view_of_delft_PUBLIC/lidar/training/calib'

    @property
    def point_cloud_file_path(self) -> Path:
        """
        Returns the full path to the point cloud data directory.

        Returns:
            Path: The Path object pointing to the point cloud data directory.
        """
        return self.__root_dir / self._point_cloud_path

    @property
    def label_file_path(self) -> Path:
        """
        Returns the full path to the label data directory.

        Returns:
            Path: The Path object pointing to the label data directory.
        """
        return self.__root_dir / self._label_path

    @property
    def indices_file_path(self) -> Path:
        """
        Returns the full path to the indices' directory.

        Returns:
            Path: The Path object pointing to the indices' directory.
        """
        return self.__root_dir / self._indices_path

    @property
    def train_indices_file_path(self) -> Path:
        """
        Returns the full path to the file containing the training set indices.

        Returns:
            Path: The Path object pointing to the training set indices file.
        """
        return self.__root_dir / self._train_indices_path

    @property
    def test_indices_file_path(self) -> Path:
        """
        Returns the full path to the file containing the test set indices.

        Returns:
            Path: The Path object pointing to the test set indices file.
        """
        return self.__root_dir / self._test_indices_path

    @property
    def pose_file_path(self) -> Path:
        """
        Returns the full path to the pose data directory.

        Returns:
            Path: The Path object pointing to the pose data directory.
        """
        return self.__root_dir / self._pose_path

    @property
    def image_file_path(self) -> Path:
        """
        Returns the full path to the image data directory.

        Returns:
            Path: The Path object pointing to the image data directory.
        """
        return self.__root_dir / self._image_path

    @property
    def calib_file_path(self) -> Path:
        """
        Returns the full path to the calibration data directory.

        Returns:
            Path: The Path object pointing to the calibration data directory.
        """
        return self.__root_dir / self._calib_path
