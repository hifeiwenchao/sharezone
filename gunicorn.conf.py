import multiprocessing


# 绑定的ip与端口
bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = 'error.log'
accesslog = 'access.log'
# 日志等级
# loglevel = 'debug'
# 进程名
proc_name = 'sharezone'
worker_class = 'gevent'
reload = True
access_log_format = '%(h)s %(l)s %(u)s %(t)s'
daemon = True
