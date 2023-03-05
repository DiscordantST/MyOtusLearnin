from .database import db
from sqlalchemy import (
    Column,
    Integer,
    String
)


class Employees(db.Model):
    id = Column(
        Integer,
        primary_key=True)
    username = Column(
        String(120),
        nullable=False)
    data_employees = Column(
        String(200),
        nullable=False,
        default="",
        server_default="")
    workplace = Column(
        String,
        nullable=False,
        unique=True
    )


