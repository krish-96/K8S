# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container at /app
COPY app.py .
COPY logger_service ./logger_service

# Make port 80 available to the world outside this container
EXPOSE 5000

## Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
