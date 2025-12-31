from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []
task_id = 1

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/tasks")
def list_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    global task_id
    new_task = {"id": task_id, **task.dict()}
    tasks.append(new_task)
    task_id += 1
    return new_task

@app.put("/tasks/{id}")
def complete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return {"message": "Task deleted"}
