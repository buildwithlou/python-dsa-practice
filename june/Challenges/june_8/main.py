###REST API has 4 main operations called CRUD: Create, Read, Update, Delete
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator
from typing import Optional, List
import httpx #this is a sync version of requests

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
async def get_tasks(skip : int = 0, limit: int = 10): #<- Async form
    return {"tasks": tasks[skip:skip + limit]}

#Add a new task
@app.post("/tasks", status_code = status.HTTP_201_CREATED)
async def create_task(task: Task):
    #check for duplicate IDs
    for existing in tasks:
        if existing["id"] == task.id:
            raise HTTPException(
                status_code = 400,
                detail= f"Task with id  {task.id} already exists"
            )
    tasks.append(task.model_dump())
    return {"message": "Task created!", "task": task}

#Get single task by ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return {"task": task}
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

#Put Update a task
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.model_dump()
            return {"message": "Task updated!", "task": tasks[i]}
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

#Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": f"Task {task_id} deleted!"}
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

#get a github username
@app.get("/github/{username}")
async def get_github_user(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        if response.status_code == 404:
            raise HTTPException(status_code = 404, detail = "Github user not found")
        return response.json()