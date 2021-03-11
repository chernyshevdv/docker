# Base image
FROM python:alpine

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]