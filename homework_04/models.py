"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from sqlalchemy import Integer, Column, String, ForeignKey, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr, relationship
import config
import os

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or config.DB_URL

async_engine: AsyncEngine = create_async_engine(
        url=PG_CONN_URI,
        echo=config.DB_ECHO,
    )

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> table_users
        Post -> table_posts
        """
        return f"table_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String(50), unique=False, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String, default=False, nullable=False)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User(username={self.username!r}, name={self.name})"


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("table_users.id"),
        nullable=False,
        unique=False,
    )
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return f"{self.__class__.name}(name={self.name!r}, user_id={self.user_id})"


