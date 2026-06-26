# Itertools are advanced Iterators
import itertools

players = ["Carlos", "Maria", "Ana"]
pairs = list(itertools.combinations(players, 2))
print(pairs)

orders = list(itertools.permutations(["A", "B", "C"]))
print(orders)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined = list(itertools.chain(list1, list2, list3))
print(combined)

colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors))

# Pathlib modern way to handle file paths, you learned os for file paths before. pathlib is the modern replacement
# from pathlib import Path
# p = Path("my_folder/my_file.txt")
# print(p.exists())
# print(p.name)
# print(p.suffix)
# print(p.parent)
# Path("new_folder").mkdir(exist_ok=True)
# content = Path("file.txt").read_text()
# Path("file.txt").write_text("Hello World")
# for file in Path(".").iterdir():
#     print(file)
# for file in Path(".").glob("*.py"):
#     print(file)

# from pathlib import Path
# path = Path("folder") / "subfolder" / "file.txt"

# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json())
# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# data = response.json()
# print(data)

# json       → store and read tasks from JSON file
# os/pathlib → check if tasks.json exists, create it if not
# datetime   → createdAt and updatedAt timestamps
# sys        → read command line arguments (sys.argv)
# re         → validate user input if needed
