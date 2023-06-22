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

def predict_image(img):
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    results = model.predict(image, conf=0.25)
    display_predictions(results)

def predict_video(video):
    while True:
        ret, frame = video.read()
        if not ret:
            break
        results = model.predict(frame, conf=0.25)
        display_predictions(results)
        
def display_predictions(results):
    for pred in results.pred:
        pred.show()


def main():
    st.title("Object Detection App")
    st.write("Upload an image or a video file to get predictions.")

    # Add file uploader
    file = st.file_uploader("Upload Image or Video", type=["jpg", "jpeg", "png", "mp4"])

    if file is not None:
        if file.type.startswith('image'):
            # Process uploaded image
            img = Image.open(file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
            predict_image(img)
        elif file.type.startswith('video'):
            # Process uploaded video
            video = cv2.VideoCapture(file)
            st.video(file)
            predict_video(video)

if __name__ == '__main__':
    main()
