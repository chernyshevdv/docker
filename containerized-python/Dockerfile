# base image
FROM python:alpine

# set working directory in the container
WORKDIR /code

# copy config files to the container working 
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy files from src to the container working directory
COPY src/ .

# command to run on container start
CMD [ "python", "server.py" ]