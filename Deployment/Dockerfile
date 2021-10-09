FROM ubuntu:latest

RUN apt update -y && apt upgrade -y && \
    apt install -y python3 python3-pip python3-venv && \
    pip3 install --upgrade pip && \
    apt install netcat curl -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1
ENV PYTHONENCODING UTF-8
ENV PYTHONPATH /

COPY ../App/requirements.txt /App/
WORKDIR /App
RUN python3 -m venv ./venv && . venv/bin/activate && pip install -r requirements.txt

COPY ../App/code_folder /App/code_folder
COPY ../App/tests /App/tests
COPY ../App/entrypoint_tests.sh /App/
COPY ../App/entrypoint.sh /App/
RUN chmod +x /App/entrypoint_tests.sh
