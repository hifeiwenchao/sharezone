import time
import random
from django.core import signing
from django.core.signing import BadSignature
import configparser
from django.conf import settings
import os


config_path = os.path.join(settings.BASE_DIR, 'config.ini')
_parser = configparser.ConfigParser()
_parser.read(config_path)


def config(section, option):
    return _parser.get(section, option)


def current_timestamp():
    """
    当前时间戳，精确到毫秒
    :return:
    """
    return int(time.time() * 1000)


def generate_order_no():
    """
    生成订单号
    :return:
    """
    return time.strftime('%Y%m%d%H%M%S') + str(random.randint(100000000, 999999999))


def obj2dict(obj):
    if isinstance(obj, dict):
        return obj

    data = {}
    for k, v in obj.__dict__.items():
        if k[0] == '_':
            continue
        data[k] = v
    return data


def encrypt(obj):
    """
    :param object obj: 需要加密的数据
    :return:  加密后字符串
    """
    value = signing.dumps(obj, salt='api')
    value = signing.b64_encode(value.encode()).decode()
    return value


def decrypt(src):
    """
    解密
    :param src: 加密的字符串
    :return:
    """
    raw = None
    try:
        src = signing.b64_decode(src.encode()).decode()
        raw = signing.loads(src, salt='api')
    except UnicodeDecodeError as e:
        pass
    except BadSignature as e:
        pass
    return raw


if __name__ == '__main__':
    print(current_timestamp())
    print(generate_order_no())

    # print(encrypt(dict(uid='1')))
    # print(decrypt('ZXlKMWFXUWlPaUl4SW4wOjFnOWlDQTpubHFVclRVeGtNR1h6c01wYnFiRFNrV0Z1cVk'))
