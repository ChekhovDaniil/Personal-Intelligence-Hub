from datetime import datetime
from typing import Any

from pydantic import BaseModel

from hub.events.models import Event


class TradingViewPayload(BaseModel):
    type: str
    occurred_at: datetime
    subject: str
    data: dict[str, Any]


def to_event(payload: TradingViewPayload) -> Event:
    return Event(
        source="tradingview",
        type=payload.type,
        occurred_at=payload.occurred_at,
        subject=payload.subject,
        data=payload.data,
    )