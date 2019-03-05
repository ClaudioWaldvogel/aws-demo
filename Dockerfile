FROM python:3.7-alpine3.8

EXPOSE 8081

COPY src /app/src/
COPY setup.py /app/setup.py

RUN apk add --update curl \
 && pip install --upgrade pip \
 && pip install -e /app/ \
 && rm -rf /var/cache/apk/*

ENTRYPOINT ["python", "/app/src/translater.py"]