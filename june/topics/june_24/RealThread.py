import time
from concurrent.futures import ThreadPoolExecutor

import requests

servers = [
    "https://api/github.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com",
    "https://api.github.com/users/buildwithlou",
]


def check_health(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start
        status = "UP" if response.status_code == 200 else "ISSUE"
        return f"{status} {url} ({duration:.2f}s)"
    except Exception as e:
        return f"DOWN {url} ({str(e)})"


# Check all servers concurrently
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(check_health, servers))

print(f"\nHealth Check Report ({time.time() - start:.2f}s total):")
print("-" * 50)
for result in results:
    print(result)
