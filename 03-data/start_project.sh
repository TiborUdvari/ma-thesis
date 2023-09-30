#!/bin/bash

# Define the image name
IMAGE_NAME="custom-datascience-notebook"

# Check if the Docker image exists
docker images | grep -w "$IMAGE_NAME" > /dev/null 2>&1

# $? is a special variable that holds the exit code of the last command executed
if [ $? -eq 0 ]; then
  echo "Docker image $IMAGE_NAME already exists."
else
  echo "Docker image $IMAGE_NAME does not exist. Building..."
  docker build -t $IMAGE_NAME .
fi

# Run the Docker container
docker run -it --rm -p 8888:8888 -v $(pwd):/home/jovyan/work $IMAGE_NAME