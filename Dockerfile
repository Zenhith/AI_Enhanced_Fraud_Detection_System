FROM python:3.9

# Install system dependencies required for building Python packages (e.g. Prophet, psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpython3-dev \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables and create folder for persistent data (if using SQLite)
ENV PORT=8000
EXPOSE 8000
RUN mkdir -p /app/data

# Run the application
CMD [ "python", "main.py" ]
