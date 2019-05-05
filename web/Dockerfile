FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /web

WORKDIR /web

COPY requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY . .

CMD python manage.py migrate --noinput
CMD python manage.py runserver 0:8000