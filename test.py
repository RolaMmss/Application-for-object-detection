import streamlit as st
import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image

# Set Streamlit app configuration
st.set_page_config(layout="wide")

# Load pre-trained YOLO model weights
model = torch.hub.load("yolov8n.pt")

# Define Streamlit app layout
st.title("Car Logo Detection with YOLO")
st.write("Upload an image to detect car logos.")

# Implement the logic for image uploading, inference, and drawing bounding boxes
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and preprocess the uploaded image
    image = Image.open(uploaded_file)
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = transforms.ToTensor()(img)

    # Make predictions using YOLO model
    results = model(img)

    # Draw bounding boxes on the detected car logos
    for detection in results.pred:
        if detection["label"] == "car_logo":
            box = detection["bbox"].tolist()
            score = detection["score"].item()
            label = detection["label"]
            img = cv2.rectangle(
                img,
                (int(box[0]), int(box[1])),
                (int(box[2]), int(box[3])),
                (0, 255, 0),
                2
            )
            img = cv2.putText(
                img,
                f"{label}: {score}",
                (int(box[0]), int(box[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2,
            )

    # Display the image with bounding boxes
    st.image(img, use_column_width=True)

# Run the Streamlit app
# Run the Streamlit app
st.set_option('deprecation.showfileUploaderEncoding', False)
