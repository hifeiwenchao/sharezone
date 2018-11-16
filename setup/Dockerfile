FROM nginx

COPY ["nginx/upstream.conf", "/etc/nginx/conf.d"]
COPY ["packages/Python-3.6.5.tgz", "/opt"]
COPY ["docker-entrypoint.sh", "/opt"]

RUN apt-get update \
    && apt-get install -y wget git gcc make zlib1g* libssl-dev libmagic-dev \
    && rm -f /etc/nginx/conf.d/default.conf
    && cd /opt \
    && wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz \
    && tar xzvf Python-3.6.5.tgz \
    && cd Python-3.6.5 \
    && ./configure --with-ssl \
    && make \
    && make install \
    && cd /opt \
    && git clone https://www.github.com/feiwencaho/sharezone.git \
    && cd sharezone \
    && pip3 install -r requirements.txt -i https://pypi.douban.com/simple \
    && gunicorn sharezone.wsgi -c gunicorn.conf.py \
    # 清理环境
    && apt-get remove -y wget git gcc make

EXPOSE 80 8000

CMD ["/opt/docker-entrypoint.sh"]

ENTRYPOINT ["sh"]
