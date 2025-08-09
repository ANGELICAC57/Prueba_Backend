from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Producto
from app.database import init_db, get_session
from uuid import UUID

app = FastAPI(title="Productos Service")

# Crear tablas al iniciar la app
@app.on_event("startup")
def on_startup():
    init_db()

# Crear un producto
@app.post("/productos")
def crear_producto(producto: Producto, session: Session = Depends(get_session)):
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return {
        "data": {
            "type": "producto",
            "id": str(producto.id),
            "attributes": producto.dict()
        }
    }

# Obtener producto por ID
@app.get("/productos/{id}")
def obtener_producto(id: UUID, session: Session = Depends(get_session)):
    producto = session.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {
        "data": {
            "type": "producto",
            "id": str(producto.id),
            "attributes": producto.dict()
        }
    }

# Listar todos los productos
@app.get("/productos")
def listar_productos(session: Session = Depends(get_session)):
    productos = session.exec(select(Producto)).all()
    return {
        "data": [
            {"type": "producto", "id": str(p.id), "attributes": p.dict()}
            for p in productos
        ]
    }
