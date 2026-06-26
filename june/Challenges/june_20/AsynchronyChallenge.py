import asyncio
import time

import httpx


async def fetch_github_user(username):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        data = response.json()
        return {
            "username": username,
            "repos": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
        }


async def fetch_sequential(usernames):
    results = []
    for u in usernames:
        result = await fetch_github_user(u)
        results.append(result)
    return results


async def main():
    usernames = ["buildwithlou", "torvalds", "gvanrossum", "yyx990803"]
    start = time.time()
    await fetch_sequential(usernames)
    sequential_time = time.time() - start
    print(f"Sequential: {sequential_time:.2f}s")

    start = time.time()
    results = await asyncio.gather(*[fetch_github_user(u) for u in usernames])
    concurrent_time = time.time() - start
    print(f"Concurrent: {concurrent_time:.2f}s")

    for result in results:
        print(
            f"{result['username']}: {result['repos']} repos, {result['followers']} followers"
        )

    print(f"\nSpeedup: {sequential_time / concurrent_time:.2f}x faster")


asyncio.run(main())
