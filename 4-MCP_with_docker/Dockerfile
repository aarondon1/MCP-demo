FROM python:3.11.8-slim

# Upgrade system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

# Install uv for faster package management
RUN pip install --no-cache-dir uv

# Copy requirements file
COPY requirements.txt .

# Install dependencies using uv
RUN uv venv
RUN uv pip install -r requirements.txt

# Copy application code
COPY server.py .
COPY client.py .

# Expose the port the server runs on
EXPOSE 8050

# Command to run the server
CMD ["uv", "run", "server.py"]