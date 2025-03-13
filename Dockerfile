FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Use a default port if not set
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Use CMD with explicit port handling
CMD gunicorn --bind 0.0.0.0:${PORT:-8000} main:app
