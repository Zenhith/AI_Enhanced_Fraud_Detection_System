FROM python:3.13-slim

# Minimize layer size
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files
COPY main.py fds.py ./

# Set memory and performance environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV GUNICORN_CMD_ARGS="--workers 2 --threads 2 --max-requests 1000 --timeout 120"

# Install production WSGI server
RUN pip install gunicorn

# Use gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "main:app"]
