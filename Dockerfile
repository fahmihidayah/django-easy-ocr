FROM python:3.9-alpine

RUN mkdir /project
COPY ./project /project
COPY requirements.txt /
COPY gunicorn.conf.py /
COPY db.sqlite3 /

RUN mkdir logs

RUN apk update  \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache libffi-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo \
    && apk del build-deps


RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["python3", "project/manage.py", "runserver", "0.0.0.0:8888"]
CMD ["gunicorn", "-c", "gunicorn.conf.py", "project.wsgi"]
