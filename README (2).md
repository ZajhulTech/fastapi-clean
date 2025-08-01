
# FastAPI Clean Architecture Project

Este proyecto sigue una arquitectura limpia usando FastAPI y MongoDB.

## ✅ PASO 1: Preparar el entorno

### 1.1 Descomprimir el proyecto

Descomprime el archivo `fastapi-clean.zip` en tu máquina. Dentro deberías ver esta estructura:

```
fastapi-clean/
├── app/
├── tests/
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md
```

## ✅ PASO 2: Levantar MongoDB con Docker

### 2.1 Verificar Docker

Asegúrate de tener Docker instalado y corriendo:

```bash
docker --version
```

### 2.2 Levantar MongoDB

Desde la terminal, ubícate dentro del proyecto:

```bash
cd fastapi-clean
docker-compose up -d
```

Esto debería levantar un contenedor con MongoDB escuchando en `localhost:27017`.

Verifica con:

```bash
docker ps
```

Deberías ver algo como:

```
CONTAINER ID   IMAGE     ...   PORTS
...            mongo     ...   0.0.0.0:27017->27017/tcp
```

## ✅ PASO 3: Instalar dependencias de Python

Recomiendo crear un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate      # en Unix/Mac
venv\Scripts\activate       # en Windows
```

Luego instala las dependencias:

```bash
pip install -r requirements.txt
```

## ✅ PASO 4: Ejecutar FastAPI

Ubícate en la raíz del proyecto (donde está `requirements.txt`) y ejecuta:

```bash
uvicorn app.webapi.main:app --reload
```

Si todo está correcto verás algo como:

```
Uvicorn running on http://127.0.0.1:8000
```

Puedes acceder a:

- Documentación interactiva: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json
