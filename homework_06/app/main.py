import os
from datetime import datetime

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from models import db, migrate_db, Posts

# указываем с каким конфигом будет происходить запуск приложения
config_name = os.getenv("CONFIG_NAME", "ProductionConfig")

# присваиваем переменной инициализацию Flask
app = Flask(__name__)

# указываем откуда брать данные для переменной config_name
app.config.from_object(f"config.{config_name}")

# инициализируем базу данных для приложения
db.init_app(app)

# делаем миграцию данных
migrate_db.init_app(app, db)


def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).one_or_404(description=f"post {post_id} not found")
    if post is None:
        abort(404)
    return post


@app.cli.command("create-all")
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', posts=Posts.query.all())


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Заголовок обязателен для заполнения')
        else:
            post = Posts(
                content=content,
                title=title
            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Заголовок обязателен для заполнения')
        else:
            post = Posts.query.get(id)
            post.title, post.content = title, content
            post.created = datetime.now()
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST', ))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    flash('"{}" was successfully deleted!'.format(post.title))
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()



