from pydantic import BaseModel

class Task(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completada: bool = False

class TaskCreate(BaseModel):
    titulo: str
    descripcion: str
    completada: bool = False