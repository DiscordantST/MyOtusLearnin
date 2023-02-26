import asyncio
from homework_04.create_data_in_tables.create_user import create_user


async def find_user(users_list: list, session) -> str:
    tasks = {
        asyncio.create_task(
            create_user(session=session,
                        name=user['name'],
                        username=user['username'], email=user['email']
                        )
        )
        for user in users_list
    }
    await asyncio.wait(tasks)
