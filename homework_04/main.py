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

from models import async_engine, Base, User, Post, Session
from jsonplaceholder_requests import users, posts


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with Session() as session:
        async with session.begin():
            async def fetch_user(users_list: list) -> str:
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

            async def fetch_post(posts_list: list) -> str:
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

            await asyncio.gather(
                fetch_user(users),
                fetch_post(posts)

            )
            await session.commit()


async def create_user(session: AsyncSession, name: str, username: str, email: str) -> User:
    user = User(name=name,
                username=username,
                email=email)
    session.add(user)
    # await session.commit()
    return user


async def create_post(session: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id,
                title=title,
                body=body)
    session.add(post)
    # await session.commit()
    return post


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
