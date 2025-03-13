# 1) Start from a Python base image
FROM python:3.9

# 2) Install system dependencies needed for Prophet and other packages
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

# 3) Create a working directory in the container
WORKDIR /app

# 4) Copy in your requirements file
COPY requirements.txt /app/

# 5) Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy the rest of your source code
COPY . /app

# 7) Set an environment variable for the port (Railway may override it)
ENV PORT=8000

# 8) Expose the port (mostly for local reference – not strictly needed on Railway)
EXPOSE 8000

# 9) By default, store the SQLite DB in /app/data so you can mount a volume there for persistence
#    Make sure your code uses a similar path for the DB:
#    engine = create_engine("sqlite:////app/data/ai_fraud_reports.db")
RUN mkdir -p /app/data

# 10) Run your main Python entrypoint
CMD [ "python", "main.py" ]
