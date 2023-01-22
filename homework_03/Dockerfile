FROM python:3.8


WORKDIR /usr/src/homework_03/
RUN pip3 install fastapi uvicorn
RUN pip3 freeze -> requirements.txt
RUN pip3 install -r requirements.txt
COPY . /usr/src/homework_03/

WORKDIR /usr/src/homework_03/view/

CMD uvicorn main:app --host 0.0.0.0

