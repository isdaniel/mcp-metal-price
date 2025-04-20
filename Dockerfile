FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install dependencies, ignoring the Python version check
RUN pip install --upgrade pip \
    && pip install --ignore-requires-python --no-cache-dir .

# Entrypoint to start the server
CMD ["python", "src/mcp_metal_price/server.py"]
