<p align="center">
  <strong>
    <h1 align="center">Object Detection & Tracking with 4D Radar Point Clouds</h1>
  </strong>
</p>
<p align="center">
   Nick Timaskovs K00260158
   <br>
  <a href='https://github.com/nicktmv' target='_blank'>GitHub nicktmv</a>&emsp;
</p>
<p align="center">
  <br>
A Final Year Project submitted to the Technological University of the Shannon in partial fulfilment of the Bachelor of Science (Honours) in Software Development degree requirements.</p>


## Aim
To achieve object detection & tracking in 4D radar point clouds.

## Dataset Preparation

First, please request and download the View of Delft (VoD) dataset from the [VoD official website](https://tudelft-iv.github.io/view-of-delft-dataset/).
There will be form to request access

Please also obtain the tracking annotation from [VoD GitHub](https://tudelft-iv.github.io/view-of-delft-dataset/docs/ANNOTATION.html). Unzip all the `.txt` tracking annotation files into the path: `view_of_delft_PUBLIC/lidar/training/label_2_tracking/`

The dataset folder structure should look like this:

```
view_of_delft_PUBLIC/
├── lidar
│   ├── ImageSets
│   ├── testing
│   └── training
│       ├── calib
│       ├── image_2
│       ├── label_2
│           ├── 00000.txt
│           ├── 00001.txt
│           ├── ...
│       ├── label_2_tracking
│           ├── 00000.txt
│           ├── 00001.txt
│           ├── ...
│       ├── pose
│       └── velodyne
├── radar
│   ├── testing
│   └── training
│       ├── calib
│       └── velodyne
├── radar_3frames
│   ├── testing
│   └── training
│       └── velodyne
└── radar_5frames
    ├── testing
    └── training
        └── velodyne
```
## Requirements

* [Python &ge; 3.8](https://www.python.org/downloads/) - Python is a programming language that lets you work quickly and integrate systems more effectively.

### IDEs

* [PyCharm](https://www.jetbrains.com/pycharm/) - The Python IDE for data science and web development.
* [Jupyter Notebook](https://jupyter.org/) - An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

### Source Code Management

* [Git](https://git-scm.com/) is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
* [GitHub Desktop](https://desktop.github.com/) - Simple collaboration from your desktop
* [WinMerge](https://winmerge.org/) is an Open Source differencing and merging tool for Windows.

### Online Tools

* [GitHub](https://www.github.com) is a web-based hosting service for version control using Git. It offers all the distributed version control and source code management (SCM) functionality of Git as well as adding its features.
* [gitignore.io](https://www.toptal.com/developers/gitignore) - Create useful .gitignore files for your project
* [plantuml.com](https://plantuml.com/) - Open-source tool that uses simple textual descriptions to draw UML diagrams.

## Machine Spec Used 🛠️
1. Intel(R) Core(TM) i7-9750H CPU
2. 16.0 GB RAM
3. NVIDIA GeForce GTX 1660 Ti

## Getting Started 🚀
<mark> Please ensure you running with an Nvidia GPU (at least 2GB VRAM).</mark>

<mark>CUDA 11.8 is required for pointnet2 dependencies. Any other configuration is not guaranteed to work.</mark>


1. Clone the repository

    ```bash
    git clone https://github.com/nicktmv/4d-radar-fyp-thesis
    ```

2. Install dependencies
   * With Pip

   ```bash
   pip install -r requirements.txt
   ```

   * With conda

   ```bash
   conda install --file requirements.txt
   ```
   
3. Install the `pointnet2` package

    ```bash
    cd RaTrack\lib
    python setup.py install
    ```

## Training the model

To train the model, please run in the terminal

```bash
python python main.py --config configs.yaml
```
This will use the `config.yaml` configuration file to train the model.

## Evaluation
To evaluate the trained model, please run:
```bash
python python main.py --config configs_eval-sw-test.yaml
```
The `configs_eval.yaml` is located in `RaTrack/checkpoints/track4d_radar/models`.

You can specify the exact model you want to evaluate by changing the `model_path` in the `configs_eval.yaml` file.

#
![Alt text for the GIF](https://github.com/nicktmv/four-d-radar-thesis/blob/refactor/docs/images/4d-radar-track-predictions.gif)


