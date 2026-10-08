from datetime import datetime, timezone

from hub.events.models import Event


def test_event_can_be_created():
    event = Event(
        source="tradingview",
        type="indicator.cross",
        occurred_at=datetime.now(timezone.utc),
        subject="LINKUSDT",
        data={
            "direction": "up",
            "timeframe": "4h",
            "price": 21.43,
        },
    )

    assert event.source == "tradingview"
    assert event.type == "indicator.cross"
    assert event.subject == "LINKUSDT"
    assert event.data["price"] == 21.43