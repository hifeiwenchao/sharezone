from api.models import SignLog
import time
import datetime


def create(**kwargs):
    return SignLog.objects.create(**kwargs)


def check_sign(user):
    """
    是否已经签到
    :return:
    """
    # 当天0点时间戳
    zero_timestamp = time.mktime(datetime.date.today().timetuple()) * 1000
    return SignLog.objects.filter(user=user, created_at__gte=zero_timestamp).exists()


if __name__ == '__main__':
    print(time.strptime('2018-10-10 00:00:00', '%Y-%m-%d %H:%M:%S'))
    print(time.strftime('%H:%M:%S', time.strptime('2018-10-10 03:10:05', '%Y-%m-%d %H:%M:%S')))
    print(time.mktime(time.strptime('2018-10-10 00:00:03', '%Y-%m-%d %H:%M:%S')))
    print(time.mktime(datetime.date.today().timetuple()))

