
FROM python:3.11-slim

WORKDIR /streamlit

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /streamlit

RUN pip install --upgrade pip && \ 
    pip install --no-cache-dir -r requirements.txt

COPY yolov8n.pt /streamlit

COPY . /streamlit.py

EXPOSE 8501

CMD ["python", "streamlit", "run", "streamlit.py", "--server.port", "8501"]
