from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from homework_04.models import Post


async def create_post_data(session: AsyncSession, data_posts) -> List[Post]:
    posts = [Post(user_id=attr_post.get('userId'),
                  title=attr_post.get('title'),
                  body=attr_post.get('body'))
             for attr_post in data_posts]
    session.add_all(posts)
    await session.commit()
    return posts
