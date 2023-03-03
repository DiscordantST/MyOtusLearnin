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
COPY . /homework_06
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000
#
CMD gunicorn app:"create_app()" -b 0.0.0.0:5000 --reload