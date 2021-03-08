# Base image
FROM python:alpine

# Add appcode to /code inside container image
ADD . /code

# Set working directory for subsequent commands
WORKDIR /code

# Install dependencies
RUN pip install -r requirements.txt

# Command to run when conatiner starts
ENTRYPOINT [ "python", "app.py" ]