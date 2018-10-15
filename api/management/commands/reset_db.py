from django.core.management.base import BaseCommand, CommandError
import pymysql
from django.db import connection
from django.conf import settings


connect = pymysql.connect(
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],

)

cursor = connect.cursor()
cursor.execute('DROP DATABASE IF EXISTS yiqibnb')
cursor.execute('CREATE DATABASE yiqibnb DEFAULT CHARSET utf8 COLLATE utf8_general_ci')
cursor.close()

exit(0)


class Command(BaseCommand):
    pass
