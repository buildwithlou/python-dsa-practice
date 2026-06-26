students = [
    {"name": "Carlos", "grade": 95},
    {"name": "Maria", "grade": 78},
    {"name": "Ana", "grade": 88},
    {"name": "Bob", "grade": 72},
    {"name": "Eve", "grade": 91},
]


def bubble_sort(students):
    arr = students[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j]["grade"] > arr[j + 1]["grade"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return [(s["name"], s["grade"]) for s in arr]


print(bubble_sort(students))
