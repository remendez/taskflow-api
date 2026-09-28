\# TaskFlow API



API REST para gestión de tareas hecha con FastAPI. La hice para practicar una arquitectura limpia con Python y tener un CRUD completo listo para dockerizar y desplegar.



\### Stack

\- Python 3.11

\- FastAPI

\- Pydantic

\- Uvicorn

\- Docker



\### Endpoints

La API tiene 7 endpoints:



\- `GET /` - Health check

\- `GET /tasks` - Lista todas las tareas

\- `POST /tasks` - Crea una tarea nueva

\- `GET /tasks/{id}` - Obtiene una tarea por ID

\- `PUT /tasks/{id}` - Actualiza una tarea

\- `DELETE /tasks/{id}` - Elimina una tarea

\- `GET /docs` - Documentación interactiva (Swagger)



\### Como correrlo local



1\. Clona el repo:

```bash

git clone https://github.com/remendez/taskflow-api.git

cd taskflow-api

