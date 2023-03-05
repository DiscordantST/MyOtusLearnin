# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /homework_06
# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /homework_06
RUN pip install --upgrade pip -r requirements.txt
RUN pip freeze > requirements.txt
# копируем содержимое папки, где находится Dockerfile,
# в рабочую директорию контейнера
COPY . /homework_06/
# Устанавливаем порт, который будет использоваться для сервера
#EXPOSE 5555

# running Flask as a module
CMD ["sh", "-c", "sleep 5 \
#    # ! run init only the first time you launch the stack and when the migrations folder do not exist yet
#    && flask create-all \
#    && flask db init \
#    # ! To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
#    && flask db stamp head \
#    && flask db migrate \
#    && flask db upgrade \
    && gunicorn wsgi:app -b 0.0.0.0:5555 --reload"]


