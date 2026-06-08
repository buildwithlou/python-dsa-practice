# with json_file("data.json") as data:
#     data.append({"name": "Carlos", "grade": 95})
#     data.append({"name": "Maria", "grade": 87})

# # After the block — data.json should contain both entries
# # Verify by opening the file again
# with json_file("data.json") as data:
#     for item in data:
#         print(item)

# Opens a JSON file — creates it with [] if it doesn't exist
# Loads the data and yields it
# On exit — saves the data back to the file automatically

import json
from contextlib import contextmanager
from pathlib import Path

@contextmanager
def json_file(file):
    path = Path(file)
    if not path.exists():
        path.write_text("[]")
        print(f"{file} created!")
    with open(path, "r") as f:
        data = json.load(f)
    try:
        yield data
    finally:
        with open(path, "w") as f:
            json.dump(data,f , indent=4)

with json_file("data.json") as data:
    data.append({"name": "Carlos", "grade": 95})
    data.append({"name": "Maria", "grade": 87})

with json_file("data.json") as data:
    for item in data:
        print(item)
