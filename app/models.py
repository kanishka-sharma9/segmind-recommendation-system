from sqlalchemy import Column, Integer, String, Text
from db import Base

class ModelInfo(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    tags = Column(String)  # comma-separated tags
