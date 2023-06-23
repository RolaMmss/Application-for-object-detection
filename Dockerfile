<<<<<<< HEAD
=======
# #Cette ligne spécifie l'image de base pour le conteneur Docker. Dans ce cas, elle utilise l'image python:3.11-slim, qui fournit un environnement Python 3.11 minimal.
# FROM python:3.11-slim

# # Cela définit le répertoire de travail à l'intérieur du conteneur sur /streamlit.
# WORKDIR /streamlit

# # Cela définit la variable d'environnement PYTHONUNBUFFERED à 1, ce qui garantit que la sortie de Python n'est pas mise en mémoire tampon, permettant un affichage en temps réel des journaux.
# ENV PYTHONUNBUFFERED 1

# # Cela copie le fichier requirements.txt de l'hôte vers le répertoire /streamlit à l'intérieur du conteneur.
# COPY requirements.txt /streamlit

# # installe les dépendances requises spécifiées dans requirements.txt 
# RUN  pip install -r requirements.txt
#     # ls
# COPY . /streamlit

# EXPOSE 8501

# CMD ["python", "streamlit", "run", "streamlit.py", "--server.port", "8501"]
# Cette ligne spécifie l'image de base pour le conteneur Docker. Dans ce cas, elle utilise l'image python:3.11-slim, qui fournit un environnement Python 3.11 minimal.
>>>>>>> 2032a13 (readme)
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /streamlit

# Copy requirements.txt to the docker container
COPY requirements.txt /streamlit

<<<<<<< HEAD
# RUN apt-get update && \
#     apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx gcc libglib2.0-0

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \ 
    libglib2.0-0    

# Install python dependencies
RUN pip install -r requirements.txt 

=======
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx gcc libglib2.0-0

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt 

>>>>>>> 2032a13 (readme)
# Copy the current directory contents into the container at /app
COPY . .

# Run the streamlit command when the container launches
CMD ["streamlit", "run", "streamlit.py", "--server.port=80", "--server.address=0.0.0.0"]
