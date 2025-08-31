from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    valor = Column(Float, nullable=False)
