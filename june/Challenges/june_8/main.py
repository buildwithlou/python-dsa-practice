###REST API has 4 main operations called CRUD: Create, Read, Update, Delete
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#Data Model - defines what a task looks like
class Task(BaseModel):
    id: int
    title: str
    status: str = "todo"                #default value
    description: Optional[str] = None   #optional field  

#In memory storage for now
tasks = []

#Get all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

#Add a new task
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.model_dump())
    return {"message": "Task created!", "task": task}

#Get single task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return {"task": task}
    return {"error": "Task not found"}

#Put Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.model_dump()
            return {"message": "Task updated!", "task": updated_task}
    return {"error": "Task not found"}

#Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": f"Task {task_id} deleted!"}
    return {"error": "Task not found"}