from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from homework_04.models import User


async def create_user_data(session: AsyncSession, data_users) -> List[User]:
    users = [User(name=attr_users.get('name'),
                  username=attr_users.get('username'),
                  email=attr_users.get('email'))
             for attr_users in data_users]
    session.add_all(users)
    await session.commit()
    return users
