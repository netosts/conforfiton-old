from fastapi import FastAPI
import asyncpg
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def connect_to_database():
    return await asyncpg.create_pool(
        host='localhost',
        port=5432,
        user='postgres',
        password='2509',
        database='conforfit_db'
    )


@app.on_event("startup")
async def startup():
    app.state.pool = await connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()


async def get_user(user_id: int):
    query = "SELECT * FROM pessoa WHERE id = $1"
    async with app.state.pool.acquire() as connection:
        result = await connection.fetchrow(query, user_id)
        return result


async def get_users(limit: int):
    query = "SELECT * FROM pessoa ORDER BY id LIMIT $1"
    async with app.state.pool.acquire() as connection:
        result = await connection.fetch(query, limit)
        return result


@app.get('/')
async def home():
    return 'Hello world!'


@app.get('/user/{user_id}')
async def read_user(user_id: int):
    user = await get_user(user_id)
    return user


@app.get('/users')
async def read_users(limit: int = 10):
    users = await get_users(limit)
    return users
