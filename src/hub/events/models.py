from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    source: str
    type: str
    occurred_at: datetime
    subject: str
    data: dict[str, Any]