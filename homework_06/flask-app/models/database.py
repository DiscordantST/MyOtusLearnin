__all__ = ('db', 'migrate_db',)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# инициализируем базу данных
db = SQLAlchemy()

# инициализируем миграцию

migrate_db = Migrate()

