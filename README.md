# fastapi-notification

This project provides a minimal FastAPI application exposing a websocket
endpoint for sending and receiving notifications.

## Running the server

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

Connect to `ws://localhost:8000/ws/notifications` from a websocket client
to send and receive messages.

## Managing packages with uv

You can use the [uv](https://github.com/astral-sh/uv) tool to manage your
Python environment. The following example creates a virtual environment and
installs the project requirements using uv:

```bash
# create a new virtual environment in .venv
uv venv .venv

# activate the environment (bash/zsh)
source .venv/bin/activate

# install the dependencies with uv's pip wrapper
uv pip install -r requirements.txt

# run the server through uv
uv run uvicorn app.main:app --reload
```

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t fastapi-notification .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 fastapi-notification
   ```
