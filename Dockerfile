# Use Python base image
FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Install Node.js and npm (for Tailwind and other frontend tasks)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Copy the entire app to the container
COPY . /app/

# Install npm packages (make sure package.json exists)
RUN npm install

# Expose port 8000 for Django
EXPOSE 8000
