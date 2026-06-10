###REST API has 4 main operations called CRUD: Create, Read, Update, Delete
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional, List

app = FastAPI()

#Data Model - defines what a task looks like
class Task(BaseModel):
    id: int
    title: str
    status: str = "todo"                #default value
    description: Optional[str] = None   #optional field  

  # Validator — runs automatically when data comes in
    @field_validator("status")
    def validate_status(cls, value):
        allowed = ["todo", "in-progress", "done"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value

    @field_validator("title")
    def validate_title(cls, value):
        if len(value) < 3:
            raise ValueError("Title must be at least 3 characters")
        return value.strip()    # removes extra spaces automatically
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