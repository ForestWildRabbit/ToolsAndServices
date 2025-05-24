from fastapi import HTTPException, Query, APIRouter

from app.config import user_collection, START_USERS_NUMBER
from app.schemas import UsersLoad
from app.utils import user_to_json, fetch_json

users_router = APIRouter()


@users_router.on_event("startup")
async def startup_event():
    await user_collection.drop()
    await user_collection.create_index("id.value")

    response = await fetch_json(f"https://randomuser.me/api/?results={START_USERS_NUMBER}")
    await user_collection.insert_many(response['results'])


@users_router.get("/")
async def root():
    response = await fetch_json("https://randomuser.me/api/?results=5")
    await user_collection.insert_many(response['results'])
    print(response['results'])
    return {}


@users_router.get("/users")
async def get_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=20)):
    skip = (page - 1) * limit
    cursor = user_collection.find().skip(skip).limit(limit)
    users = await cursor.to_list(length=limit)
    for user in users:
        user_to_json(user)

    return users


@users_router.get("/random")
async def get_random_user():
    result = await user_collection.aggregate([{"$sample": {"size": 1}}]).to_list(length=1)
    if result:
        user = result[0]
        return user_to_json(user)
    else:
        raise HTTPException(status_code=404, detail="No users found")


@users_router.get("/{user_id}")
async def get_user(user_id: str):
    user = await user_collection.find_one({"id.value": user_id})
    if user:
        return user_to_json(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@users_router.post("/load/{users_count}")
async def load_users(users_load: UsersLoad):
    return users_load.number

