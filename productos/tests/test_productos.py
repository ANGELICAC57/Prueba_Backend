import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_producto():
    response = client.post("/productos", json={
        "nombre": "Laptop",
        "precio": 2500.50,
        "descripcion": "Laptop de prueba"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["attributes"]["nombre"] == "Laptop"

def test_listar_productos():
    response = client.get("/productos")
    assert response.status_code == 200
    assert "data" in response.json()
