import aiohttp


async def get_data_for_url(url_data: str) -> list:  # get data for url, using aiohttp
    async with aiohttp.ClientSession().get(url_data, ssl=True) as url_data:
        return await url_data.json()
