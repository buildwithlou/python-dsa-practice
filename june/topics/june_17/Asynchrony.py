# async def         # defines a coroutine (async function)
# await             # pause here, let other tasks run
# asyncio.run()     # entry point — runs the async program
import asyncio
import time


# Asynchronous - does both at the same time
async def make_coffee():
    print("Boiling water...")
    await asyncio.sleep(3)  # yield control, doesn't block
    print("Coffee ready!")


async def make_toast():
    print("Toasting bread...")
    await asyncio.sleep(2)  # yield control, doesn't block
    print("Toast ready!")


async def main():
    await asyncio.gather(make_coffee(), make_toast())


start = time.time()
asyncio.run(main())
print(f"Total: {time.time() - start:.2f}s")  # 3 seconds
