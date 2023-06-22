# !pip install streamlit
# !pip install ultralytics

import cv2
import streamlit as st
from PIL import Image, ImageDraw
from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.yaml")
model.load("yolov8n.pt")

# # Class labels for car makes
# class_labels = ['Audi', 'BMW', 'Mercedes', 'MercedesBenz', 'Toyota', 'Volkswagen', 'toyota']


def main():
    st.title("Prédire la marque de voiture!")
    st.write("Upload an image or a video file to predict the car make.")

    # Add file uploader
    file = st.file_uploader("Upload Image or Video", type=["jpg", "jpeg", "png", "mp4"])

    if file is not None:
        if file.type.startswith('image'):
            # Process uploaded image
            img = Image.open(file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
            results= model(img)
            # results = model.predict(img, conf=0.25)

           # Display predicted labels on the image
            # annotated_img = results.render()  # Render annotated image with bounding boxes and labels
            # annotated_img = Image.fromarray(annotated_img)  # Convert the image array to PIL Image
            # st.image(img, caption='Predicted Image', use_column_width=True)
            
        
            # Plot the results on the image
            res_plotted = results[0].plot(labels=True)
            st.image(res_plotted, caption='Predicted Image', use_column_width=True)
            
            # Display the predicted image
            # st.image(img, caption='Predicted Image', use_column_width=True)
            # res=results[0].plot()
            # st.image(res)
        elif file.type.startswith('video'):
            # Process uploaded video
            video = cv2.VideoCapture(file)
            st.video(file)
            results= model(video)
            # Display predicted labels on the video frames
            annotated_video = results.render()  # Render annotated video frames with bounding boxes and labels
            st.video(annotated_video)
            # res=results[0].plot()
            # st.image(res)

if __name__ == '__main__':
    main()

