# Store Inventory API

> **Una API REST moderna, asíncrona y orientada a producción para la gestión de inventarios.**

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</div>

## 📌 Descripción del Proyecto
Este repositorio es una demostración técnica de **Backend Generalista**. Implementa un CRUD (Crear, Leer, Actualizar, Borrar) completo utilizando los estándares actuales de la industria para microservicios de alto rendimiento.

En lugar de usar frameworks pesados (como Django) o código síncrono legado, esta API utiliza **FastAPI** junto con soporte asíncrono puro (`asyncpg`) para hablar con **PostgreSQL**. Esto garantiza tiempos de respuesta mínimos y máxima concurrencia.

## ⚙️ Arquitectura Técnica
- **Framework:** FastAPI (Python 3.11+)
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (Async Engine)
- **Validación & Serialización:** Pydantic V2
- **Orquestación:** Docker & Docker Compose

## 🚀 Instalación y Despliegue Local

Con `docker-compose`, levantar el entorno (que incluye la base de datos y la API en redes segregadas) requiere un solo comando:

```bash
git clone https://github.com/franamaro-dev/Store-Inventory-API.git
cd Store-Inventory-API

# Levanta Postgres y FastAPI en segundo plano
docker-compose up -d --build
```

### 📖 Autodocumentación Interactiva (Swagger UI)
FastAPI genera automáticamente la documentación interactiva OpenAPI. Una vez que los contenedores estén corriendo, visita:
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

## 🛠️ Patrones de Diseño Implementados
1.  **Repository Pattern Acoplado:** Separación estricta entre las rutas (`routers/`), validación de contratos de entrada/salida (`schemas.py`), modelos de base de datos (`models.py`) y transacciones puras (`crud.py`).
2.  **Inyección de Dependencias:** Gestión segura de las sesiones de base de datos (`async_sessionmaker`) inyectadas directamente en los endpoints mediante `Depends()`.
3.  **Gestión de Variables de Entorno:** Utilización segura de `pydantic-settings` para la configuración del entorno.
