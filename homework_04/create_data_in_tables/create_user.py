from homework_04.models import User
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, name: str, username: str, email: str) -> User:
    user = User(name=name,
                username=username,
                email=email)
    session.add(user)
    return await user
