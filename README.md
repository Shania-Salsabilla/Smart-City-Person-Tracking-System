# Smart-City-Person-Tracking-System

## Introduction:
Urban security is a critical concern for modern cities. An intelligent AI-based person-tracking system can significantly enhance surveillance capabilities, allowing for the automatic detection and tracking of individuals in specific areas to ensure safety and security. This project leverages advanced object detection algorithms, Faster R-CNN and YOLOv8m, to develop a robust person-tracking system. Person tracking involves detecting objects in the initial frame and then tracking them across subsequent frames. Object Detection techniques generate bounding boxes around objects of interest, which are then used for tracking purposes.

## Dataset:
The dataset used in this project is COCO (Common Objects in Context) 2017, a popular dataset for training and evaluating object detection models. It contains over 200,000 labeled images with 80 object categories. The dataset can be accessed from Kaggle at the following link: [COCO 2017 Dataset](https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset).

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
3. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install the required packages:
   pip install -r requirements.txt

