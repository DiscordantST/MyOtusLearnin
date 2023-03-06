from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://user:pass@pg:5432/table_homework_6"  # адрес коннекта к БД
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = ""
    SECRET_KEY = "very_secret_key" # для каждой среды (прод, дев, тест) необходимо использовать свой ключ
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = "testing"
    DEBUG = True
    SQLALCHEMY_ECHO = True



