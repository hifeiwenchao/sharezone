# Generated by Django 2.1.1 on 2018-10-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181015_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(null=True, upload_to='upload', verbose_name='头像'),
        ),
    ]
