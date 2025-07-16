# FastMCP Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv for Python package management
RUN pip install uv

# Copy dependency files (will be created in later tasks)
COPY pyproject.toml uv.lock* ./

# Install Python dependencies using uv
RUN uv sync --frozen

# Copy source code
COPY . .

# Expose port
EXPOSE 8001

# Start the FastMCP server
CMD ["uv", "run", "python", "server.py"]