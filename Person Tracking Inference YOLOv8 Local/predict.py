import torch
from ultralytics import YOLO

import cv2

# Check if CUDA (GPU support) is available and set the device
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# pretrained model nano
# model = YOLO("models/yolov8n.pt").to(device)
# pretrained model medium
model = YOLO("models/yolov8m.pt").to(device)
# finetuned model
# model = YOLO("models/yolov8m_person_epoch50.pt").to(device)

cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(
            frame,
            conf=0.5,
            iou=0.45,
            show_labels=True,
            show_conf=True,
            classes=[0],
            verbose=False,
        )

        # Visualize the results on the frame
        annotated_frame = results[0].plot(labels=True)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
