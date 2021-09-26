FROM ubuntu:latest

RUN apt update -y && apt upgrade -y && \
    apt install -y python3 python3-pip python3-venv && \
    pip3 install --upgrade pip && \
    apt install netcat curl -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1
ENV PYTHONENCODING UTF-8
ENV PYTHONPATH /

COPY ../requirements.txt /Tests/pizza_exercise_docker/
WORKDIR /Tests/pizza_exercise_docker/
RUN python3 -m venv ./venv && . venv/bin/activate && pip install -r requirements.txt


COPY ../code_folder /Tests/pizza_exercise_docker/code_folder
COPY ../tests /Tests/pizza_exercise_docker/tests
COPY ../entrypoint_tests.sh /Tests/pizza_exercise_docker/
RUN chmod +x /Tests/pizza_exercise_docker/entrypoint_tests.sh
