FROM python:3.8


WORKDIR /usr/src/homework_03/
RUN pip install fastapi uvicorn
RUN pip freeze -> requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/homework_03/

WORKDIR /usr/src/homework_03/view/

CMD uvicorn main:app --host 0.0.0.0

