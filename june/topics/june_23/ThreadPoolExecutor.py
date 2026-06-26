import time
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch_url(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"


urls = [
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://api.github.com/users/buildwithlou",
]

# Sequential
start = time.time()
results = [fetch_url(url) for url in urls]
print(f"Sequential:{time.time() - start:.2f}s")

# Threaded
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch_url, urls))
print(f"Threaded: {time.time() - start:.2f}s")

for r in results:
    print(r)
