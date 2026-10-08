from fastapi import FastAPI

from hub.events.models import Event
from hub.integrations.tradingview import TradingViewPayload, to_event

app = FastAPI(title="Intelligence & Automation Hub")


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/webhooks/tradingview", response_model=Event)
def tradingview_webhook(payload: TradingViewPayload) -> Event:
    return to_event(payload)