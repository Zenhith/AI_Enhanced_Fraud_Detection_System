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

# Install dependencies including gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application files
COPY . .

# Make run script executable
RUN chmod +x run.sh

# Use a default port if not set
ENV PORT=8080

# Expose the port
EXPOSE ${PORT}

# Run using the run script which has a fallback mechanism
CMD ["./run.sh"]
