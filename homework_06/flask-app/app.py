import os
from http import HTTPStatus

from flask import Flask, render_template, request, flash, redirect
from wtforms import StringField, validators
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired

from models import db, migrate_db
from models.employees import Employees

# указываем с каким конфигом будет происходить запуск приложения
config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

# присваиваем переменной инициализацию Flask
app = Flask(__name__)

# указываем откуда брать данные для переменной config_name
app.config.from_object(f"config.{config_name}")

# инициализируем базу данных для приложения
db.init_app(app)

# делаем миграцию данных
migrate_db.__init__(app=app, db=db)


csrf = CSRFProtect(app)


@app.cli.command("create-all")
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


@app.route('/', methods=["GET", "POST"])
def index_page():
    return render_template('index.html',  items=Employees.query.all())


class Employees_form(FlaskForm):
    username = StringField("ФИО", [validators.Length(min=3, max=100), DataRequired()])
    data_employees = StringField("Описание", [validators.Length(min=3, max=100), DataRequired()])


@app.route('/create', methods=["GET", "POST"])
def create_page():
    form = Employees_form()
    if request.method == "GET":
        return render_template("create_employees.html", form=form)

    if not form.validate_on_submit():
        return (
            render_template("create_employees.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    employees = Employees(
            username=form.data["username"],
            data_employees=form.data["data_employees"])
    db.session.add(employees)
    db.session.commit()
    flash(f"Product {employees.username} was created!", category="success")
    return redirect('/')


if __name__ == "__main__":
    app.run()


