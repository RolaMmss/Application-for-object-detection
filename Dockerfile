# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /streamlit

# Copy requirements.txt to the docker container
COPY requirements.txt /streamlit

# RUN apt-get update && \
#     apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx gcc libglib2.0-0

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \ 
    libglib2.0-0    

# Install python dependencies
RUN pip install -r requirements.txt 

# Copy the current directory contents into the container at /app
COPY . .

# Run the streamlit command when the container launches
CMD ["streamlit", "run", "streamlit.py", "--server.port=80", "--server.address=0.0.0.0"]
