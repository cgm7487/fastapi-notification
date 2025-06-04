FROM python:3.11-slim
WORKDIR /app

# Install uv and project dependencies
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
