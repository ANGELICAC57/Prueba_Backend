# 📦 Microservicio de Productos

Este microservicio gestiona el catálogo de productos, permitiendo listar, registrar y consultar productos específicos.

## 🚀 Tecnologías usadas
- Python 3.13
- FastAPI
- SQLModel
- SQLite (puede cambiarse a otro motor)
- Docker

## 📌 Instalación y ejecución

### Clonar repositorio
```bash
git clone https://github.com/ANGELICAC57/Prueba_Backend.git
cd productos
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
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

## 📜 Variables de entorno
```env
# Puerto y base de datos
DATABASE_URL=sqlite:///./productos.db
```

## 🐳 Ejecución con Docker
```bash
docker build -t productos-service .
docker run -p 8001:8001 --env-file .env productos-service
```

## 🧪 Ejecución de pruebas
```bash
pytest --cov=app --cov-report=term-missing
```

## 📚 Documentación de la API
- Swagger UI: [http://localhost:8001/docs](http://localhost:8001/docs)
- Redoc: [http://localhost:8001/redoc](http://localhost:8001/redoc)
