from four_d_radar.utils.data_paths import DataPaths  # Ensure you import DataPaths correctly from wherever it's defined


def main():
    root_dir = "D:/four-d-radar-thesis"
    paths = DataPaths(root_dir)
    print(paths.data_path)


if __name__ == "__main__":
    main()
