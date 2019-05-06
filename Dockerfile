FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /exchange_rate_crawler

WORKDIR /exchange_rate_crawler

COPY ./requirements.txt ./requirements.txt
COPY ./scrapyd.conf /etc/scrapyd/

RUN pip install -r ./requirements.txt

COPY . .

CMD python manage.py runserver 0:8000

#ENTRYPOINT ["/bin/sh", "run.sh"]