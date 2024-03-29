"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from data_json.get_json_data import get_data_for_url

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data(users_data_url: str) -> list:  # get data for USERS_DATA_URL
    return await get_data_for_url(users_data_url)


async def fetch_post_data(post_data_url: str) -> list:  # get data for POSTS_DATA_URL
    return await get_data_for_url(post_data_url)


