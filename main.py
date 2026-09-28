from fastapi import FastAPI, HTTPException
from schemas import Task, TaskCreate

app = FastAPI(
    title="TaskFlow API",
    description="API REST demostrativa para gestión de tareas",
    version="1.0.0"
)

tasks_db = [
    {
        "id": 1,
        "titulo": "Aprender FastAPI",
        "descripcion": "Crear una API REST con Python y FastAPI",
        "completada": False
    },
    {
        "id": 2,
        "titulo": "Subir proyecto a GitHub",
        "descripcion": "Publicar TaskFlow API como proyecto de portafolio",
        "completada": False
    }
]

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a TaskFlow API", "estado": "ok", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks", response_model=list[Task])
def obtener_tareas():
    return tasks_db

@app.post("/tasks", response_model=Task, status_code=201)
def crear_tarea(tarea: TaskCreate):
    nuevo_id = max([t["id"] for t in tasks_db], default=0) + 1
    nueva_tarea = {"id": nuevo_id, **tarea.model_dump()}
    tasks_db.append(nueva_tarea)
    return nueva_tarea

@app.get("/tasks/{task_id}", response_model=Task)
def obtener_tarea(task_id: int):
    for tarea in tasks_db:
        if tarea["id"] == task_id:
            return tarea
    raise HTTPException(status_code=404, detail=f"Tarea con id {task_id} no encontrada")

@app.put("/tasks/{task_id}", response_model=Task)
def actualizar_tarea(task_id: int, tarea_actualizada: TaskCreate):
    for index, tarea in enumerate(tasks_db):
        if tarea["id"] == task_id:
            tasks_db[index] = {"id": task_id, **tarea_actualizada.model_dump()}
            return tasks_db[index]
    raise HTTPException(status_code=404, detail=f"Tarea con id {task_id} no encontrada")

@app.delete("/tasks/{task_id}")
def eliminar_tarea(task_id: int):
    for index, tarea in enumerate(tasks_db):
        if tarea["id"] == task_id:
            del tasks_db[index]
            return {"mensaje": f"Tarea {task_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail=f"Tarea con id {task_id} no encontrada")