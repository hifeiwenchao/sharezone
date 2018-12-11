FROM nginx

COPY ["setup/nginx/upstream.conf", "/etc/nginx/conf.d"]
COPY ["setup/packages/Python-3.6.5.tgz", "/opt"]
COPY ["setup/docker-entrypoint.sh", "/opt"]
COPY ["./", "/opt/sharezone"]
WORKDIR /opt/sharezone

RUN apt-get update \
    && apt-get install -y wget gcc make zlib1g* libssl-dev libmagic-dev \
    && rm -f /etc/nginx/conf.d/default.conf \
    && cd /opt \
    && wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz \
    && tar xzvf Python-3.6.5.tgz \
    && cd Python-3.6.5 \
    && ./configure --with-ssl \
    && make \
    && make install \
    && cd /opt/sharezone \
#    && git clone https://www.github.com/feiwencaho/sharezone.git \
#    && cd sharezone \
    && pip3 install -r requirements.txt -i https://pypi.douban.com/simple \
#    && gunicorn sharezone.wsgi -c gunicorn.conf.py \
    # 清理环境
    && apt-get remove -y wget gcc make
    # 启动NGINX
#    && nginx -g 'daemon off;'
#    && nginx



EXPOSE 80 8000

CMD ["nginx", "-g", "daemon off;"]

#CMD ["/opt/docker-entrypoint.sh"]

#ENTRYPOINT ["sh"]
