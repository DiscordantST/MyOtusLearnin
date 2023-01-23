# Для развертывания образа необходим Docker, проверить установлен ли Docker можно командой в терминале: docker version
# https://www.docker.com скачать Docker можно с официального сайта
# после установки докера можно проверить доступные images, команда: docker images
# для создания образа необходимо выполнить следующую коммандуL docker build -t homework_03 ./homework_03
# проверить создание образа командой: docker images
# для запуска контейнера выполнить команду: docker run homework_03

FROM python:3.10-buster

WORKDIR /usr/src/homework_03/

RUN pip install fastapi uvicorn
RUN pip freeze -> requirements.txt

COPY . /usr/src/homework_03/

WORKDIR /usr/src/homework_03/view/

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0

