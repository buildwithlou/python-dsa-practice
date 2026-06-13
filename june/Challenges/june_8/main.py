###REST API has 4 main operations called CRUD: Create, Read, Update, Delete
from fastapi import FastAPI, HTTPException, status, Depends, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from typing import Optional, List
import time, httpx #this is a sync version of requests

app = FastAPI()
#This would send an email or Slack message
def send_notification(task_title: str):
    print(f"Sending email: task '{task_title}' was created!")

#Get all tasks
@app.get("/tasks")
async def get_tasks(
    skip: int = 0,
    limit: int = 10,
    token: str = Depends(verify_token)): #<- Async form ( allows for non blocking operations, enabling multiple requests)
    return {"tasks": tasks[skip: skip + limit]}

#Add a new task
@app.post("/tasks", status_code = status.HTTP_201_CREATED)
async def create_task(
    task: Task, 
    background_tasks: BackgroundTasks,
    token: str = Depends(verify_token)
):
    #checking duplicate IDs
    for existing in tasks:
        if existing["id"] == task.id:
            raise HTTPException(
                status_code = 400,
                detail= f"Task with id {task.id} already exists"
            )
    tasks.append(task.model_dump())
    background_tasks.add_task(send_notification, task.title)
    return {"message": "Task created!", "task": task}

#Get single task by ID
@app.get("/tasks/{task_id}")
async def get_task(
    task_id: int,
    token: str = Depends(verify_token)
    ):
    for task in tasks:
        if task["id"] == task_id:
            return {"task": task}
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

#Put Update a task
@app.put("/tasks/{task_id}")
async def update_task(
    task_id: int, 
    updated_task: Task,
    token: str = Depends(verify_token)
    ):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.model_dump()
            return {"message": "Task updated!", "task": tasks[i]}
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

#Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    token: str = Depends(verify_token)
    ):
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
    
