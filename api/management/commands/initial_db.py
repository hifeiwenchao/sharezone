from django.core.management.base import BaseCommand, CommandError
import pymysql
from django.db import connection
from django.conf import settings
from collections import namedtuple
from api.models import Area, Category


def format_fetch(cursor):
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


class Command(BaseCommand):
    help = '初始化数据库'

    def handle(self, *args, **options):
        connect = pymysql.connect(
            host='127.0.0.1',
            port=3308,
            user='yiqibnb',
            password='1qaz#EDC',
            db='yiqibnb'
        )
        cursor = connect.cursor()
        cursor.execute('select * from dict where class_id=0')
        rows = format_fetch(cursor)
        # rows = cursor.fetchall()
        self.stdout.write('初始化Area...')
        area_count = 0
        for row in rows:
            existed = Area.objects.filter(name=row.c_name, identity=row.s_class_id).exists()
            if not existed:
                Area.objects.create(
                    name=row.c_name,
                    identity=row.s_class_id,
                    pid=row.p_id
                )
                area_count += 1
        self.stdout.write(self.style.SUCCESS('初始化Area完成, 插入%s条数据' % area_count))

        self.stdout.write('初始化Category...')
        cursor.execute('select * from share_category')
        rows = format_fetch(cursor)
        category_count = 0
        for row in rows:
            existed = Category.objects.filter(name=row.category_name)
            if not existed:
                Category.objects.create(
                    name=row.category_name,
                    pid=row.p_id
                )
                category_count += 1
        self.stdout.write(self.style.SUCCESS('初始化Category完成, 插入%s条数据' % category_count))

        cursor.close()




