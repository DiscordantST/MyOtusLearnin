"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from data_json.get_json_data import get_data_for_url

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def find_users_data(users_data_url: str) -> list:  # get data for USERS_DATA_URL
    return await get_data_for_url(users_data_url)


async def find_post_data(post_data_url: str) -> list:  # get data for POSTS_DATA_URL
    return await get_data_for_url(post_data_url)


users = asyncio.run(find_users_data(USERS_DATA_URL))  # list data users
posts = asyncio.run(find_post_data(POSTS_DATA_URL))  # lists data posts
