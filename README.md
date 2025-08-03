
# FastAPI Clean Architecture Project
![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-%20green)
Este proyecto implementa una arquitectura limpia utilizando **FastAPI** y **MongoDB** como base de datos, facilitando el mantenimiento, escalabilidad y separación de responsabilidades.

---

## 🧠 Arquitectura

El proyecto sigue los principios de **Clean Architecture**, dividiendo la lógica en capas bien definidas:

```
app/
├── infra/                  # Infraestructura (API, MongoDB, respuestas)
├── interfaces/             # Contratos y puentes entre capas (repositories, unit of work, user stories)
├── models/                 # Modelos de datos (AtlasDB, request, response)
├── userstorys/             # Casos de uso / lógica de negocio
```

---

## ✅ PASO 1: Instalar dependencias de Python

Crea un entorno virtual e instala las dependencias necesarias:

```bash
python -m venv venv
source venv/bin/activate      # en Unix/Mac
venv\Scripts\activate       # en Windows

pip install -r requirements.txt
```

---

## 🚀 PASO 2: Ejecutar FastAPI

Ubícate en la raíz del proyecto y ejecuta:

```bash
uvicorn app.infra.api.main:app --reload
```

Esto levanta la API y puedes acceder a la documentación interactiva en:

- http://127.0.0.1:8000/docs

---

## 🐳 Uso con Docker

Este proyecto incluye un `docker-compose.yml` para levantar servicios fácilmente.

### Levantar los servicios:
```bash
docker-compose up --build
```

### Detener los servicios:
```bash
docker-compose down
```

---

## 🧪 Testing

> Por implementar

```bash
pytest
```

---

## 📂 Estructura de carpetas (detallada)

- `app/infra/api/` - Controladores de API y respuestas HTTP
- `app/infra/mongodb/` - Repositorios e implementación con MongoDB
- `app/interfaces/` - Interfaces base para UnitOfWork y Repositorios
- `app/models/` - Modelos de entidades, DTOs para request y response
- `app/userstorys/` - Casos de uso / lógica de negocio (Application Layer)

---

## 📌 Tecnologías utilizadas

- Python 3.10+
- FastAPI
- MongoDB
- Pydantic
- Uvicorn
- Docker / Docker Compose

---

## 🧑‍💻 Autor

Desarrollado por Saúl Dueñas B. 
© 2025

---

## 📝 Licencia

![License](https://img.shields.io/badge/License-MIT-green.svg)
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
