from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import uuid4, UUID

class Producto(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    precio: float
    descripcion: Optional[str] = None