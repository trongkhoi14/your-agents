from sqlalchemy import Column, String, Text, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from app.db import Base

class PriceTier(str, enum.Enum):
    free = "free"
    freemium = "freemium"
    paid = "paid"

class Agent(Base):
    __tablename__ = "agents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)
    price_tier = Column(Enum(PriceTier), nullable=False, default=PriceTier.freemium)
    website_url = Column(String, nullable=True)
    demo_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)