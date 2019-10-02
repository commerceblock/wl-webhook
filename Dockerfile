FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV LISTEN_PORT 10080

EXPOSE 10080


COPY ./cb_idcheck /usr/src/package
COPY ./app /app

RUN set -x \
    && mkdir -p /kycfile/whitelist \
    && mkdir -p /kycfile/consider \
    && cd /usr/src/package \
    && python3 setup.py build \
    && python3 setup.py install 

