from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.database import init_db, get_session
from app.models import Inventario
from uuid import UUID
import requests
import os

PRODUCTOS_SERVICE_URL = os.getenv("PRODUCTOS_SERVICE_URL", "http://127.0.0.1:8001")

app = FastAPI(title="Inventario Service")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/inventario/{producto_id}")
def consultar_inventario(producto_id: UUID, session: Session = Depends(get_session)):
    inv = session.get(Inventario, producto_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Producto no tiene inventario registrado")
    return {
        "data": {
            "type": "inventario",
            "id": str(producto_id),
            "attributes": {"cantidad": inv.cantidad}
        }
    }

@app.post("/inventario")
def actualizar_inventario(inventario: Inventario, session: Session = Depends(get_session)):
    if isinstance(inventario.producto_id, str):
        inventario.producto_id = UUID(inventario.producto_id)
    session.merge(inventario)
    session.commit()
    return {
        "data": {
            "type": "inventario",
            "id": str(inventario.producto_id),
            "attributes": {"cantidad": inventario.cantidad}
        }
    }

@app.post("/comprar")
def comprar_producto(producto_id: UUID, cantidad: int, session: Session = Depends(get_session)):
    if cantidad <= 0:
            raise HTTPException(status_code=400, detail="La cantidad debe ser mayor que 0")
    try:
        r = requests.get(f"{PRODUCTOS_SERVICE_URL}/productos/{producto_id}", timeout=3)
        r.raise_for_status()
        producto = r.json()["data"]["attributes"]
    except:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    inv = session.get(Inventario, producto_id)
    if not inv or inv.cantidad < cantidad:
        raise HTTPException(status_code=400, detail="Inventario insuficiente")

    inv.cantidad -= cantidad
    session.add(inv)
    session.commit()

    return {
        "data": {
            "type": "compra",
            "id": str(producto_id),
            "attributes": {
                "producto": producto,
                "cantidad_comprada": cantidad,
                "restante": inv.cantidad
            }
        }
    }
