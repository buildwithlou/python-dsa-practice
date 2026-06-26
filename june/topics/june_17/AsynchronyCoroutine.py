import asyncio


# async def - this is a coroutine, not a regular function
async def greet(name, delay):
    await asyncio.sleep(delay)  # pause without blocking
    print(f"Hello {name}!")


async def main():
    # run all there at the same time
    await asyncio.gather(greet("Carlos", 3), greet("Maria", 1), greet("Ana", 2))


asyncio.run(main())
