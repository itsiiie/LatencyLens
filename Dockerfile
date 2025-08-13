# STEP 1: Base Python image
FROM python:3.11-slim

# STEP 2: Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

# STEP 3: Set working directory
WORKDIR /app

# STEP 4: Install system dependencies
RUN apt-get update && \
  apt-get install -y netcat-traditional && \
  pip install --upgrade pip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# STEP 5: Copy requirements file and install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# STEP 6: Copy the rest of the project
COPY . /app/

# STEP 7: Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
