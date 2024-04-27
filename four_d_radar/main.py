from four_d_radar.utils.data_paths import DataPaths
from four_d_radar.utils.data_loader import run_data_loader


def main():
    root_dir = "D:/four-d-radar-thesis"

    # Initialize the DataPaths class with the root directory
    paths = DataPaths(root_dir)

    print(paths.point_cloud_file_path)

    run_data_loader(root_dir)


if __name__ == "__main__":
    main()
