# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ../requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY .. /app

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
