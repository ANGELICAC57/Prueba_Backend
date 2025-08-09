# 📊 Diagrama de Arquitectura

```
                ┌──────────────────────────┐
                │        Cliente/API        │
                └─────────────┬────────────┘
                              │
                ┌─────────────▼────────────┐
                │   Inventario Service     │
                │  (FastAPI + SQLModel)    │
                └─────────────┬────────────┘
                              │ HTTP GET /productos/{id}
                              │
                ┌─────────────▼────────────┐
                │    Productos Service     │
                │  (FastAPI + SQLModel)    │
                └─────────────┬────────────┘
                              │
                  ┌───────────▼───────────┐
                  │  Base de Datos Prod.  │
                  └───────────────────────┘
```
