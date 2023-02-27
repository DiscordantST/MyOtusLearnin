import aiohttp
from typing import List


async def get_data_for_url(url_data: str) -> list:  # get data for url, using aiohttp
    async with aiohttp.ClientSession().get(url_data, ssl=True) as url_data:
        data: List[dict] = await url_data.json()
        return data
