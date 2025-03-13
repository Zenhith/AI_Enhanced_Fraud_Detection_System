FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpython3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies first
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Create necessary directories
RUN mkdir -p /app/models /app/data

# Set environment variables
ENV PORT=8000
ENV MODEL_PATH=/app/models
ENV DATABASE_PATH=/app/data/ai_fraud_reports.db

# Expose port
EXPOSE 8000

# Use a production-ready command
CMD ["python", "main.py"]
