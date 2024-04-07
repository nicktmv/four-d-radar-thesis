import open3d as o3d
import numpy as np
import struct
import os
from four_d_radar.utils.paths import Paths
from four_d_radar.utils.data_loader import load_dataset, load_labels, load_indices, load_data_from_files


class RadarPointCloudVisualizer:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.index = 0
        self.vis = o3d.visualization.VisualizerWithKeyCallback()

    def load_point_cloud(self, index):
        # Assume that the point cloud data is in the format [x, y, z, intensity, ...]
        points = self.data[index][:, :3]  # Use only x, y, z for visualization
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points)
        return point_cloud

    def visualize(self):
        self.vis.create_window(window_name='Radar Point Cloud Visualizer')
        self.vis.add_geometry(self.load_point_cloud(self.index))

        # Key callback to close the visualizer
        self.vis.register_key_callback(262, self.next_frame)  # Right arrow key for the next frame
        self.vis.register_key_callback(81, self.close_visualizer)  # q key to close the visualizer

        self.vis.run()  # This will start the visualization loop

    def next_frame(self, vis):
        self.index += 1
        if self.index >= len(self.data):
            self.index = 0  # Loop back to the first frame

        vis.clear_geometries()  # Clear the old geometries
        vis.add_geometry(self.load_point_cloud(self.index))  # Load the new point cloud

    def close_visualizer(self, vis):
        self.vis.destroy_window()


def main():
    paths = Paths()  # Make sure the paths.py file is correctly referenced

    # Load the dataset
    print("Loading training data...")
    train_data, train_labels = load_dataset(paths.data_path, paths.label_path, paths.train_indices_path,
                                            load_labels_flag=True)

    # Initialize the visualizer with the training data
    if train_data:
        visualizer = RadarPointCloudVisualizer(train_data, train_labels)
        visualizer.visualize()
    else:
        print("No training data to visualize.")


if __name__ == "__main__":
    main()
