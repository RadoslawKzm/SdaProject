# pull official base image
FROM ubuntu:latest

RUN apt update -y && apt upgrade -y && \
    apt install -y python3 python3-pip python3-venv && \
    pip3 install --upgrade pip && \
    apt install netcat curl -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1
ENV PYTHONENCODING UTF-8
ENV PYTHONPATH /


