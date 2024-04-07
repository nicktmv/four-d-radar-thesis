import open3d as o3d
import numpy as np
import os
import struct
import tkinter as tk

# ... [Include your data loader functions here: load_indices, load_labels, load_data_from_files, load_dataset]
import four_d_radar.utils.data_loader


# Function to convert point cloud data to Open3D format and visualize
def visualize_point_cloud(points):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points[:, :3])  # assuming points has xyz as the first 3 columns
    o3d.visualization.draw_geometries([point_cloud])


# Function to load the next point cloud frame and update the visualization
def load_next_frame(data, index):
    if index[0] < len(data):
        visualize_point_cloud(data[index[0]])
        index[0] += 1
    else:
        print("No more frames to display.")


# Main function to set up the GUI and start the visualization process
def main():
    # Use the data loading functions to load your dataset
    data_path = '../../data/view_of_delft_PUBLIC/radar/training/velodyne'
    label_path = '../../data/view_of_delft_PUBLIC/lidar/training/label_2'
    indices_path = '../../data/view_of_delft_PUBLIC/lidar/ImageSets/train.txt'
    data, labels = four_d_radar.load_dataset(data_path, label_path, indices_path, load_labels_flag=True)

    # Setup a simple GUI for navigation
    root = tk.Tk()
    root.title("3D Radar Point Cloud Viewer")
    frame_index = [0]  # mutable container to keep track of the current frame
    next_frame_button = tk.Button(root, text="Next Frame", command=lambda: load_next_frame(data, frame_index))
    next_frame_button.pack()

    # Start the GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()
