FROM python:3.8

COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Installs pip requirements and copy entire app over!
RUN pip install -r requirements.txt
COPY . /app

ENV DISPLAY=:99

