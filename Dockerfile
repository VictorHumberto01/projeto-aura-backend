FROM python:3.11-slim

# Install system dependencies, including curl for the Docker healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements and install python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose Django development port
EXPOSE 8000

# Default command (overwritten in docker-compose.yml for dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
