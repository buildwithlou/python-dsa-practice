import asyncio
import time


async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"


async def main():
    start = time.time()
    r1 = await fetch_data("API 1", 2)
    r2 = await fetch_data("API 2", 2)
    r3 = await fetch_data("API 3", 2)
    print(f"Sequential: {time.time() - start:.2f}s")

    start = time.time()
    r1, r2, r3 = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 2),
        fetch_data("API 3", 2),
    )
    print(f"Concurrent: {time.time() - start:.2f}s")


asyncio.run(main())
