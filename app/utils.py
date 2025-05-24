import httpx


def user_to_json(user):
    user["_id"] = str(user["_id"])
    return user


async def fetch_json(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
