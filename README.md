# VISION: Visual Inference: Segmentation and Object Network

VISION is a web-based project for image analysis that integrates state-of-the-art models for object detection and image segmentation. Initially, it leverages the YOLO model for detection and segmentation tasks, and future iterations will incorporate additional models such as UNet and more, offering a versatile platform for various computer vision applications.

## Info.

**简体中文**  
VISION 是一个基于网络的平台，利用先进的计算机视觉模型，如 YOLO 和 UNet，实现实时目标检测和图像分割。

**繁體中文**  
VISION 是一個基於網頁的平台，利用尖端的計算機視覺模型，如 YOLO 和 UNet，來實現即時目標檢測與影像分割。

**English**  
VISION is a web-based platform that leverages cutting-edge computer vision models, such as YOLO and UNet, to perform real-time object detection and image segmentation.

**Deutsch (German)**  
VISION ist eine webbasierte Plattform, die modernste Computer-Vision-Modelle wie YOLO und UNet nutzt, um in Echtzeit Objekterkennung und Bildsegmentierung durchzuführen.

**Français (French)**  
VISION est une plateforme web qui exploite des modèles de vision par ordinateur de pointe, tels que YOLO et UNet, pour réaliser la détection d'objets et la segmentation d'images en temps réel.

**Nederlands (Dutch)**  
VISION is een webgebaseerd platform dat geavanceerde computervisie-modellen, zoals YOLO en UNet, inzet voor realtime objectdetectie en beeldsegmentatie.

**日本語 (Japanese)**  
VISION は、YOLO や UNet などの最先端のコンピュータビジョンモデルを活用し、リアルタイムで物体検出および画像セグメンテーションを実現するウェブベースのプラットフォームです。

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported Models](#supported-models)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **VISION** project is designed to provide a unified web interface for processing images and videos using cutting-edge computer vision models. Users can upload files to perform:
- **Image Detection:** Locate and classify objects within an image.
- **Image Segmentation:** Delineate objects or regions in an image with precise masks.

This platform is ideal for research, prototyping, and deployment of various computer vision tasks in a web environment.

## Features

- **Web-based Upload:** Simple user interface to upload images or videos.
- **Progress Monitoring:** Real-time progress tracking of processing tasks.
- **Multi-Model Support:** Currently includes YOLO for detection/segmentation and will expand to support UNet and other models.
- **Asynchronous Processing:** Utilizes background processing to handle time-consuming tasks without blocking the user interface.
- **Result Visualization:** Displays processed images or videos directly on the web page.

## Supported Models

- **YOLO:** Used for real-time object detection and segmentation.
- **UNet (Planned):** A popular model for image segmentation tasks.
- *Other models can be added as needed to expand the capabilities of the platform.*

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kancheng/visionwsd.git
   cd visionwsd
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download model weights:**

   Ensure you have the required model weights (e.g., `yolov8n-seg.pt` for YOLO) in the appropriate directory.

## Usage

1. **Start the Flask server:**

   ```bash
   python app.py
   ```

2. **Access the Web Interface:**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to use the upload form.

3. **Upload and Process:**

   - Select an image or video file.
   - Click "Upload" and monitor the progress.
   - View the processed result once completed.

## Project Structure

```
vision/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Front-end HTML page
├── static/
│   └── results/            # Processed results are stored here
├── uploads/                # Uploaded files are temporarily stored here
├── requirements.txt        # Python dependencies
└── README.md               # This documentation file
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
