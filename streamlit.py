# https://colab.research.google.com/drive/1i8yl9NxsgH9JlRCTzvVdA_Y2bJixI9n1#scrollTo=iiIlsue4YJrv

# !pip install streamlit
# !pip install ultralytics

import cv2
import streamlit as st
from PIL import Image, ImageDraw
from ultralytics import YOLO
import numpy as np

model = YOLO("best.pt")
# model=YOLO("yolov8n.pt")

# # Class labels for car makes
# class_labels = ['Audi', 'BMW', 'Mercedes', 'MercedesBenz', 'Toyota', 'Volkswagen', 'toyota']

# metrics = model.val() 
# print("Precision: ", metrics.results_dict['metrics/precision(B)'])
# print("Recall: ", metrics.results_dict['metrics/recall(B)'])
# print("mAP: ", metrics.results_dict['metrics/mAP50(B)'])
# print("Fitness: ", metrics.fitness)

def main():
    st.title("Prédire la marque de voiture!")
    st.write("Upload an image or a video file to predict the car make.")

    # Add file uploader
    file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if file is not None:
        if file.type.startswith('image'):
            # Process uploaded image
            img = Image.open(file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
            results= model(img)  
        
            # Plot the results on the image
            res_plotted = results[0].plot(labels=True)
            st.image(res_plotted, caption='Predicted Image', use_column_width=True)
            
        elif file.type.startswith('video'):
            # Process uploaded video
            video = cv2.VideoCapture(file)
            st.video(file)
            results= model(video)
            # Display predicted labels on the video frames
            res_plotted = results[0].plot(labels=True)
            st.video(res_plotted)
        
if __name__ == '__main__':
    main()

