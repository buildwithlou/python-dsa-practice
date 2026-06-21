import asyncio, httpx
async def fetch_github_user(username):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        data = response.json()
        return {"username": username, "repos": data.get("public_repos", 0)}
    
async def main():
    usernames = ["torvalds", "gvanrossum", "buildwithlou"]

    #Fetch all 3 profiles at the same time
    results = await asyncio.gather(*[
        fetch_github_user(u) for u in usernames
    ])

    for result in results:
        print(f"{result['username']}: {result['repos']} repos")

asyncio.run(main())