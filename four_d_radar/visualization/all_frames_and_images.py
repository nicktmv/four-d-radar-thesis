import open3d as o3d
import numpy as np
import cv2
import os

from four_d_radar.utils.data_loader import load_dataset
from four_d_radar.utils.data_paths import DataPaths


class RadarPointCloudVisualizer:
    def __init__(self, data, labels, image_path):
        self.data = data
        self.labels = labels
        self.image_path = image_path
        self.index = 0

    def load_point_cloud_image(self, index, zoom=0.5):
        # Convert point cloud to image using Open3D
        points = self.data[index][:, :3]
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points)

        vis = o3d.visualization.Visualizer()
        vis.create_window(visible=False)
        vis.add_geometry(point_cloud)

        # Set the zoom level of the view control.
        ctr = vis.get_view_control()
        ctr.set_zoom(zoom)

        vis.poll_events()
        vis.update_renderer()
        image = vis.capture_screen_float_buffer(False)
        vis.destroy_window()

        image = np.asarray(image)
        image = (image * 255).astype(np.uint8)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR format
        return image

    def load_image(self, index):
        image_filename = os.path.join(self.image_path, f"{index:05d}.jpg")
        image = cv2.imread(image_filename)
        return image

    def combine_images(self, img1, img2, border_color=(255, 255, 255), border_width=10):
        # Ensure both images have the same height
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        if h1 != h2:
            img2 = cv2.resize(img2, (int(w2 * h1 / h2), h1))

        # Create a vertical border
        border = np.full((h1, border_width, 3), border_color, dtype=np.uint8)

        # Concatenate images with a border in between
        combined_image = np.hstack((img1, border, img2))
        return combined_image

    def visualize(self):
        cv2.namedWindow('Point Cloud and Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Point Cloud and Image', 1800, 600)

        while True:
            pc_image = self.load_point_cloud_image(self.index)
            cv_image = self.load_image(self.index)
            combined_image = self.combine_images(pc_image, cv_image)

            cv2.imshow('Point Cloud and Image', combined_image)

            key = cv2.waitKey(0) & 0xFF
            if key == 262 or key == 32:  # Right arrow key or spacer to move to the next frame
                self.index += 1
                if self.index >= len(self.data):
                    self.index = 0  # Loop back to the first frame
            elif key == ord('q'):  # Press 'q' to quit
                break

        cv2.destroyAllWindows()


def main():
    data_paths = DataPaths()
    train_data, train_labels = load_dataset(data_paths.data_path, data_paths.label_path, data_paths.train_indices_path,
                                            load_labels_flag=True)

    if train_data:
        visualizer = RadarPointCloudVisualizer(train_data, train_labels, data_paths.image_path)
        visualizer.visualize()
    else:
        print("No training data to visualize.")


if __name__ == "__main__":
    main()
