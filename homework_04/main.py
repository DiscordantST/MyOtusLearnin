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

from homework_04.create_data_in_tables.create_user import create_user
from homework_04.find_data.find_user import find_user
from homework_04.find_data.find_post import find_post
from models import async_engine, Base, Session
from jsonplaceholder_requests import users, posts


async def async_main():
    async with async_engine.begin() as conn:  # Initialize the creation of tables
        await conn.run_sync(Base.metadata.drop_all)  # Drop table for avoid duplicate
        await conn.run_sync(Base.metadata.create_all)  # Create new table
    async with Session() as session:  # Open session
        async with session.begin():
            await asyncio.gather(
                find_user(users, session),
                find_post(posts, session)
            )
        await session.commit()  # commit all add users and posts
        await session.close()


def main():
    asyncio.run(async_main())  # run func async_main


if __name__ == "__main__":
    main()  # run main func
