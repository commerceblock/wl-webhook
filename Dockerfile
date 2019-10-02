FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV LISTEN_PORT 80

EXPOSE 80

WORKDIR /
COPY ./app /app

WORKDIR /
RUN git clone https://github.com/commerceblock/cb_idcheck.git

WORKDIR /cb_idcheck
RUN set -x \
    && mkdir -p /kycfile/whitelist \
    && mkdir -p /kycfile/consider \
    && python3 setup.py build \
    && python3 setup.py install 

