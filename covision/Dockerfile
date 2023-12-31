# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
# Python won't try to write .pyc files on the container
ENV PYTHONDONTWRITEBYTECODE 1
# Python buffers stdout and stderr by default, this option ensures that logs are streamed directly to the console
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Copy the requirements file into the container at /app
COPY requirements.txt /app/
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]