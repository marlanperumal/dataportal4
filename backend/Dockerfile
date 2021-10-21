FROM python:3.8

COPY requirements.docker.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD [ \
    "--worker-tmp-dir=/dev/shm", \
     "--bind=0.0.0.0:5000", \
     "--workers=4", \
     "--threads=8", \
     "--worker-class=gthread", \
     "--log-file=-", \
     "--access-logfile=-", \
     "--access-logformat='%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s'", \
     "--timeout=3600", \
     "app:app" \
]
