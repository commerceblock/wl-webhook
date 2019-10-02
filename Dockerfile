FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./cb_idcheck /usr/src/package
COPY ./app /app

RUN set -x \
    && cd /usr/src/package \
    && python3 setup.py build \
    && python3 setup.py install 

