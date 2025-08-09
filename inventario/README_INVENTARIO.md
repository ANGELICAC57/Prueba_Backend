# 📦 Microservicio de Inventario

Este microservicio gestiona las existencias de los productos y permite registrar compras, interactuando con el microservicio de Productos para validar la información.

## 🚀 Tecnologías usadas
- Python 3.13
- FastAPI
- SQLModel
- SQLite (puede cambiarse a otro motor)
- Docker
- requests (para comunicación entre microservicios)

## 📌 Instalación y ejecución

### Clonar repositorio
```bash
git clone https://github.com/ANGELICAC57/Prueba_Backend.git
cd inventario
```

### Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar servicio
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
```

## 📜 Variables de entorno
```env
PRODUCTOS_SERVICE_URL=http://127.0.0.1:8001
DATABASE_URL=sqlite:///./inventario.db
```

## 🐳 Ejecución con Docker
```bash
docker build -t inventario-service .
docker run -p 8002:8002 --env-file .env inventario-service
```

## 🧪 Ejecución de pruebas
```bash
pytest --cov=app --cov-report=term-missing
```

## 📚 Documentación de la API
- Swagger UI: [http://localhost:8002/docs](http://localhost:8002/docs)
- Redoc: [http://localhost:8002/redoc](http://localhost:8002/redoc)
