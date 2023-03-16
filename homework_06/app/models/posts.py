from .database import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from datetime import datetime


class Posts(db.Model):
    id = Column(
        Integer,
        primary_key=True,)
    created = Column(
        DateTime(),
        default=datetime.now)
    title = Column(
        String(100),
        nullable=False)
    content = Column(
        String(100),
        nullable=False)


