FROM python:3.5-jessie

COPY app.py /

RUN mkdir -p /serasa-rest-api

WORKDIR /serasa-rest-api

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD . /serasa-rest-api

ADD app.py /

EXPOSE 80

CMD ["python", "./app.py"]
