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

# Use a default port if not set
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Alternative CMD if gunicorn fails
CMD if command -v gunicorn >/dev/null 2>&1; then \
        gunicorn --bind 0.0.0.0:${PORT:-8000} main:app; \
    else \
        python main.py; \
    fi
