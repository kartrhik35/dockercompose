# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

# Copy source code into container
COPY app/ app/

# Default command to run your Flask app using module format
CMD ["python", "-m", "app.main"]
