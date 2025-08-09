# app/models.py
from uuid import UUID
from sqlmodel import SQLModel, Field

class Inventario(SQLModel, table=True):
    producto_id: UUID = Field(primary_key=True)
    cantidad: int