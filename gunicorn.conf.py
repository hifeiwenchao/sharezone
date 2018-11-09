import multiprocessing


# 绑定的ip与端口
bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = 'error.log'
accesslog = 'access.log'
# loglevel = 'debug' # 日志等级
proc_name = 'sharezone'   # 进程名
