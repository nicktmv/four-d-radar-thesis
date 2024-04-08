from four_d_radar.utils.data_paths import DataPaths


def main():
    root_dir = "D:/four-d-radar-thesis"

    # Initialize the DataPaths class with the root directory
    paths = DataPaths(root_dir)

    # Example usage: Print the absolute path to the point cloud files
    print(paths.pointcloud_file_path)


if __name__ == "__main__":
    main()
