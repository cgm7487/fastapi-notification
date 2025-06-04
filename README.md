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
