from pydantic import BaseModel

class ItemBase(BaseModel):
    nome: str
    valor: float

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    nome: str | None = None
    valor: float | None = None

class ItemOut(ItemBase):
    id: int
    class Config:
        from_attributes = True
