#!/usr/bin/env bash

cd /opt/sharezone
# 启动python服务
gunicorn sharezone.wsgi -c gunicorn.conf.py
# 启动nginx
nginx -g 'daemon off;'
