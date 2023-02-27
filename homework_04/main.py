"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models import async_engine, Base, Session
from jsonplaceholder_requests import fetch_users_data, fetch_post_data, USERS_DATA_URL, POSTS_DATA_URL
from create_data.create_user import *
from create_data.create_post import *


async def async_main():
    async with async_engine.begin() as conn:  # Initialize the creation of tables
        await conn.run_sync(Base.metadata.drop_all)  # Drop table for avoid duplicate
        await conn.run_sync(Base.metadata.create_all)  # Create new table
        users, posts = await asyncio.gather(fetch_users_data(USERS_DATA_URL),
                                            fetch_post_data(POSTS_DATA_URL))
    async with Session() as session:  # Open session
        await create_user_data(session, users)
        await create_post_data(session, posts)
    await session.close()


def main():
    asyncio.run(async_main())  # run func async_main


if __name__ == "__main__":
    main()  # run main func
