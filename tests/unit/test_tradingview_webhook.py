from fastapi.testclient import TestClient

from hub.main import app

client = TestClient(app)


def test_tradingview_webhook_creates_event():
    response = client.post(
        "/webhooks/tradingview",
        json={
            "type": "indicator.cross",
            "occurred_at": "2026-10-07T02:00:00+00:00",
            "subject": "LINKUSDT",
            "data": {
                "direction": "up",
                "timeframe": "4h",
                "price": 21.43,
            },
        },
    )

    assert response.status_code == 200

    event = response.json()

    assert event["source"] == "tradingview"
    assert event["type"] == "indicator.cross"
    assert event["subject"] == "LINKUSDT"
    assert event["data"]["price"] == 21.43