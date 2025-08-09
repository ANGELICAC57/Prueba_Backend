import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app, PRODUCTOS_SERVICE_URL
import requests_mock
from uuid import uuid4
from fastapi.testclient import TestClient

client = TestClient(app)

def test_actualizar_inventario():
    producto_id = uuid4()
    response = client.post("/inventario", json={
        "producto_id": str(producto_id),
        "cantidad": 10
    })
    assert response.status_code == 200
    assert response.json()["data"]["attributes"]["cantidad"] == 10

def test_comprar_producto():
    producto_id = uuid4()

    with requests_mock.Mocker() as m:
        m.get(f"{PRODUCTOS_SERVICE_URL}/productos/{producto_id}", json={
            "data": {
                "type": "producto",
                "id": str(producto_id),
                "attributes": {
                    "nombre": "Laptop",
                    "precio": 1000.0
                }
            }
        })

        client.post("/inventario", json={
            "producto_id": str(producto_id),
            "cantidad": 5
        })

        resp = client.post("/comprar", params={
            "producto_id": str(producto_id),
            "cantidad": 2
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["attributes"]["restante"] == 3
