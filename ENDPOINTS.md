# 📌 Tabla de Endpoints

| Servicio | Método | Endpoint | Descripción |
|----------|--------|----------|-------------|
| **Productos** | `GET` | `/productos` | Lista todos los productos |
| **Productos** | `GET` | `/productos/{id}` | Consulta un producto por ID |
| **Productos** | `POST` | `/productos` | Crea un nuevo producto |
| **Inventario** | `GET` | `/inventario/{producto_id}` | Consulta el inventario de un producto |
| **Inventario** | `POST` | `/inventario` | Actualiza o registra el inventario de un producto |
| **Inventario** | `POST` | `/comprar` | Realiza una compra y descuenta el inventario |
