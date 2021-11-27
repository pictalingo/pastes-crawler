FROM python:3.8

LABEL maintainer="dan@ados.co.il"

RUN apt-get update && apt-get -y install cron

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

COPY ./cron /etc/cron.d/cron

RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron
RUN touch /var/log/cron.log

CMD sudo chmod +x /code/finder.py
CMD cron && tail -f /var/log/cron.log
