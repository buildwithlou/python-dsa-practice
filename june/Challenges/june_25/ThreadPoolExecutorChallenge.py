from concurrent.futures import ThreadPoolExecutor
import requests
import time

servers = [
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://www.google.com",
    "https://api.github.com/users/buildwithlou"
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
    
#Sequential
start = time.time()
sequential_results = [check_health(url) for url in servers]
sequential_time = time.time() - start
print(f"Sequential: {sequential_time:.2f}s")

#Check all servers concurrently
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(check_health, servers))
concurrent_time = time.time() - start


print(f"\nHealth Check Report ({time.time() - start:.2f}s total):")
print("-" * 50)
for result in results:
    print(result)