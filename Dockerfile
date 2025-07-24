# Use the official Python 3.11 slim image as the base image
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install Python dependencies listed in requirements.txt without using cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to allow communication to/from the container
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "app.py"]
