# 4d-radar-fyp-thesis

## Aim
To explore the theoretical methodology of achieving object detection from raw 4D radar point clouds

## Dataset Preparation

First, please request and download the View of Delft (VoD) dataset from the [VoD official website](https://tudelft-iv.github.io/view-of-delft-dataset/).

Please also obtain the tracking annotation from [VoD GitHub](https://github.com/tudelft-iv/view-of-delft-dataset/blob/main/docs/ANNOTATION.md). Unzip all the `.txt` tracking annotation files into the path: `view_of_delft_PUBLIC/lidar/training/label_2_tracking/`

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

* [Python 3.11](https://www.python.org/downloads/) - Python is a programming language that lets you work quickly and integrate systems more effectively.

### IDEs

* [PyCharm](https://www.jetbrains.com/pycharm/) - The Python IDE for data science and web development.

### Source Code Management

* [Git](https://git-scm.com/) is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
* [GitHub Desktop](https://desktop.github.com/) - Simple collaboration from your desktop
* [WinMerge](https://winmerge.org/) is an Open Source differencing and merging tool for Windows.

### Online Tools

* [GitHub](https://www.github.com) is a web-based hosting service for version control using Git. It offers all the distributed version control and source code management (SCM) functionality of Git as well as adding its features.
* [gitignore.io](https://www.toptal.com/developers/gitignore) - Create useful .gitignore files for your project
* [plantuml.com](https://plantuml.com/) - Open-source tool that uses simple textual descriptions to draw UML diagrams.

## 🚀 Getting Started

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


