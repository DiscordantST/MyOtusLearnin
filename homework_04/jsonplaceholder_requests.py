"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

from data_json.get_json_data import get_data_for_url

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


class User:
    name: str
    username: str
    email: str


async def fetch_users_data(users_data_url: str) -> list:  # get data for USERS_DATA_URL
    return await get_data_for_url(users_data_url)


async def fetch_post_data(post_data_url: str) -> list:  # get data for POSTS_DATA_URL
    return await get_data_for_url(post_data_url)
#
#
users = asyncio.run(fetch_users_data(USERS_DATA_URL))
posts = asyncio.run(fetch_post_data(POSTS_DATA_URL))



