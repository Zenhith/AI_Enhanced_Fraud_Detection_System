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
ENV PORT=8080

# Expose the port
EXPOSE ${PORT}

# Create startup script
RUN echo '#!/bin/bash\n\
if [ "$GUNICORN_ENABLED" = "false" ]; then\n\
    echo "Running with Python directly..."\n\
    python main.py\n\
else\n\
    echo "Running with Gunicorn..."\n\
    # Extended timeout to allow for initialization\n\
    gunicorn --bind 0.0.0.0:${PORT} --workers=1 --threads=2 --timeout=300 wsgi:application\n\
fi' > /app/start.sh && chmod +x /app/start.sh

# Run with the startup script
CMD ["/app/start.sh"]
