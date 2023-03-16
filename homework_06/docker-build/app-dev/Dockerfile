FROM tiangolo/uwsgi-nginx-flask:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD [ "sh" , "-c" , "sleep 2 \
#    && flask db stamp head \
#    && flask db migrate \
    && flask db upgrade \
    && flask run --host=0.0.0.0" ]