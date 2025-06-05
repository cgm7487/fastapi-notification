import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_single_client_echo():
    with client.websocket_connect("/ws/notifications") as websocket:
        websocket.send_text("hello")
        data = websocket.receive_text()
        assert data == "hello"


def test_broadcast_and_disconnect():
    with client.websocket_connect("/ws/notifications") as ws_receiver:
        with client.websocket_connect("/ws/notifications") as ws_sender:
            ws_sender.send_text("ping")
            assert ws_sender.receive_text() == "ping"
            assert ws_receiver.receive_text() == "ping"
        # sender disconnected
        assert ws_receiver.receive_text() == "A client disconnected"
