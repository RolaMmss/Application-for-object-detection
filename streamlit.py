# !pip install streamlit
# !pip install ultralytics

import cv2
import streamlit as st
from PIL import Image
# from google.colab.patches import cv2_imshow
from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.yaml")
model.load("yolov8n.pt")

# # Class labels for car makes
# class_labels = ['Audi', 'BMW', 'Mercedes', 'MercedesBenz', 'Toyota', 'Volkswagen', 'toyota']

# def predict_image(img):
#     # Convert image to OpenCV format
#     image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
#     # Perform object detection using the YOLOv8 model
#     results = model.predict(image, conf=0.25)
    

def main():
    st.title("Car Mark")
    st.write("Upload an image or a video file to predict the car make.")

    # Add file uploader
    file = st.file_uploader("Upload Image or Video", type=["jpg", "jpeg", "png", "mp4"])

    if file is not None:
        if file.type.startswith('image'):
            # Process uploaded image
            img = Image.open(file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
            # predict_image(img)
            results = model.predict(img, conf=0.25)
            res=results[0].plot()
            # cv2_imshow(res)
            st.image(res)
        elif file.type.startswith('video'):
            # Process uploaded video
            video = cv2.VideoCapture(file)
            st.video(file)
            # predict_video(video)
            results = model.predict(video, conf=0.25)
            res=results[0].plot()
            st.image(res)

if __name__ == '__main__':
    main()

