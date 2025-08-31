from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Item
from .schemas import ItemCreate, ItemOut, ItemUpdate

app = FastAPI(title="Demo API (FastAPI + Postgres)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = Item(nome=payload.nome, valor=payload.valor)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items", response_model=list[ItemOut])
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, payload: ItemUpdate, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    if payload.nome is not None:
        item.nome = payload.nome
    if payload.valor is not None:
        item.valor = payload.valor
    db.commit()
    db.refresh(item)
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db.delete(item)
    db.commit()
    return None
