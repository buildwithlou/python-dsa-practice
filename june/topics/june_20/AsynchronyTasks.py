import asyncio


async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"


async def main():
    task1 = asyncio.create_task(worker("Task A", 3))
    task2 = asyncio.create_task(worker("Task B", 1))
    task3 = asyncio.create_task(worker("Task C", 2))

    print("Tasks are running in background...")

    results = await asyncio.gather(task1, task2, task3)
    print(results)


asyncio.run(main())
