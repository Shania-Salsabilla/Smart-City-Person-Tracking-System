# Smart-City-Person-Tracking-System
![Saturday Afternoon Walk in Gangnam Streets Seoul Tour Korea](https://github.com/user-attachments/assets/e16edea9-c4f3-4209-8a08-9cd6bdd171c0)

## Introduction:
Urban security is a critical concern for modern cities. An intelligent AI-based person-tracking system can significantly enhance surveillance capabilities, allowing for the automatic detection and tracking of individuals in specific areas to ensure safety and security. This project leverages advanced object detection algorithms, Faster R-CNN and YOLOv8m, to develop a robust person-tracking system. Person tracking involves detecting objects in the initial frame and then tracking them across subsequent frames. Object Detection techniques generate bounding boxes around objects of interest, which are then used for tracking purposes.

## Features:
- `Dataset`: The dataset used in this project is COCO (Common Objects in Context) 2017, a popular dataset for training and evaluating object detection models. It contains over 200,000 labeled images with 80 object categories. The dataset can be accessed from Kaggle at the following link: [COCO 2017 Dataset](https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset).
- `Object Detection Algorithms`:
   1. YOLOv8m: Implementation of YOLO (You Only Look Once) algorithm version 8m for object detection.
   2. Faster R-CNN: Implementation of the Faster R-CNN algorithm for object detection.

## Folder Structure:
- `Original Images for Person Tracking`: This folder contains the original images to be tracked.
- `Person Tracking Inference YOLOv8 Local`:
  This folder contains:
  1. `Models`: A folder that stores the trained YOLOv8 models.
  2. `predict.py`: The file to perform predictions with the YOLOv8 model.
  3. `requirements.txt`: A file that lists the dependencies needed to run YOLOv8.
- `Person Tracking with YOLOv8m`:
   This folder contains:
   1. `YOLOv8m Images on Test Data`: A folder that stores YOLOv8m prediction results on test data.
   2. `YOLOv8m New Images`: Folder that stores new images used for testing.
   3. `best.pt`: The best trained YOLOv8m model.
   4. `Testing YOLOv8m.ipynb`: Notebook for testing the YOLOv8m model.
   5. `Training YOLOv8m 50 Epoch.ipynb`: Notebook for training the YOLOv8m model for 50 epochs.
- `Person Tracking Inference with Gradio.ipynb`: Notebook for performing inference using Gradio.
- `Person Tracking with Faster-RCNN.ipynb`: Notebook for training and testing models with Faster R-CNN.
- `Person Detection.pptx`: A PowerPoint file that presents project details, including the results of person detection and tracking.

## Getting Started:
To reproduce and run this project on your local machine, follow these steps:

### Prerequisites:
    Ensure you have the following installed:
    - Python 3.8 or higher
    - Virtual environment tool (e.g., venv or conda)
    - Git

### Installation:
    1. Clone the repository:
       git clone https://github.com/yourusername/smart-city-person-tracking.git
       cd smart-city-person-tracking
    2. Create a virtual environment and activate it:
       python -m venv venv
       source venv/bin/activate  # On Windows use `venv\Scripts\activate`![Saturday Afternoon Walk in Gangnam Streets Seoul Tour Korea](https://github.com/user-attachments/assets/4ce11ece-456a-4a69-8431-a838b4e41d14)

    3. Install the required packages:
       pip install -r requirements.txt



