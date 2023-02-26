import asyncio
from homework_04.create_data_in_tables.create_post import create_post


async def find_post(posts_list: list, session) -> str:
    tasks = {
        asyncio.create_task(
            create_post(session=session,
                        user_id=post['userId'],
                        title=post['title'], body=post['body']
                        )
        )
        for post in posts_list
    }
    await asyncio.wait(tasks)
