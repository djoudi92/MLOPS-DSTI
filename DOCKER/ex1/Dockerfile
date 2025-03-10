# Use a recent Python runtime as the base image
FROM python:3.12-slim

# Meta-data
LABEL maintainer="Djoudi Abdessalem <abdessalemdjoudi@gmail.com>" \
  description="Data Science Workflow #1: Self-Contained Container - Libraries, data, and code in one image"

# Set the working directory to /app
WORKDIR /app

# Install the required libraries
RUN pip install --upgrade pip && pip --no-cache-dir install numpy pandas seaborn scikit-learn jupyter

# Copy the project files
COPY . .

# Expose Jupyter Notebook port
EXPOSE 8888

# Run Jupyter when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
