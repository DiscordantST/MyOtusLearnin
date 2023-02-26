import asyncio
from homework_04.models import Post
from sqlalchemy.ext.asyncio import AsyncSession


async def create_post(session: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id,
                title=title,
                body=body)
    await asyncio.sleep(0.5)
    session.add(post)
    return post
