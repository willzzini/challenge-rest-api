FROM python:3.5-jessie

COPY app.py /

RUN mkdir -p /challenge-rest-api

WORKDIR /challenge-rest-api

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD . /challenge-rest-api

ADD app.py /

EXPOSE 80

CMD ["python", "./app.py"]
