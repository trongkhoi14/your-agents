from pydantic import BaseModel, HttpUrl
from uuid import UUID
from typing import Optional
from enum import Enum

class PriceTier(str, Enum):
    free = "free"
    freemium = "freemium"
    paid = "paid"

class AgentBase(BaseModel):
    name: str
    provider: str
    description: Optional[str] = None
    category: str
    price_tier: PriceTier
    website_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None
    is_active: bool = True

class AgentCreate(AgentBase):
    pass

class AgentRead(AgentBase):
    id: UUID

    class Config:
        orm_mode = True