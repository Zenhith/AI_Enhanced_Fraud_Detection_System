FROM python:3.9

# Install system libraries needed for building packages (like Prophet, psycopg2)
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

# Upgrade pip and installer tools
RUN pip install --upgrade pip setuptools wheel

# Install packages that Prophet depends on
RUN pip install --no-cache-dir cython
RUN pip install --no-cache-dir pystan==2.19.1.1

# Install all the Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your source code into the container
COPY . /app

# Set an environment variable for the port (Railway may override this)
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Create a directory for persistent data (if using SQLite, mount a volume to this path)
RUN mkdir -p /app/data

# Run the application
CMD [ "python", "main.py" ]
