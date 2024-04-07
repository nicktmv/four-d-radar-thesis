import four_d_radar.utils.data_loader
import four_d_radar.visualization.vis_frames_and_images


def main():
    # Load the dataset
    data, labels = four_d_radar.utils.data_loader.load_dataset()

    # Initialize the visualizer with the data and labels
    visualizer = four_d_radar.visualization.vis_frames_and_images.RadarPointCloudVisualizer(data, labels)
    visualizer.visualize()


if __name__ == "__main__":
    main()
