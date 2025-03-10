# Use an official Python runtime as a parent image
FROM python:3.12-alpine3.21

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest and any project dependencies
RUN pip install --no-cache-dir pytest

# Run pytest when the container launches
CMD ["pytest", "tests"]
