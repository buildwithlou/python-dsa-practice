from database import Task, create_db, get_session
from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select

app = FastAPI()


# Create tables on startup
@app.on_event("startup")
def startup():
    create_db()


# Get all tasks
@app.get("/tasks")
def get_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return {"tasks": tasks}


# Post create task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return {"message": "Task created!", "task": task}


# Get single task
@app.get("/tasks/{task_id}")
def get_Task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return {"task": task}


# Put update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    task.title = updated.title
    task.status = updated.status
    task.description = updated.description
    session.commit()
    session.refresh(task)
    return {"message": "Task updated!", "task": task}


# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    session.delete(task)
    session.commit()
    return {"message": f"Task {task_id} deleted!"}
