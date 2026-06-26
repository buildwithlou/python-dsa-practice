import json
from pathlib import Path

# creating a path object pointing to tasks.json
file = Path(__file__).parent / (
    "tasks.json"
)  # __file__: this variable is going to know where the current script is.

# check is the json exists, if not create it empty
if not file.exists():
    file.write_text("[]")
    print("tasks.json created!")

tasks = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build Task Tracker", "done": False},
]

file.write_text(json.dumps(tasks, indent=4))
print("Tasks saved!")

content = file.read_text()
loaded_tasks = json.loads(content)
for task in loaded_tasks:
    print(f"Task {task['id']}: {task['task']} - Done: {task['done']}")
