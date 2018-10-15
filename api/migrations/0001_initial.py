# Generated by Django 2.1.1 on 2018-10-11 09:50

import common.utils
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account', models.CharField(max_length=50, null=True, unique=True, verbose_name='账号')),
                ('phone', models.CharField(max_length=20, null=True, unique=True, verbose_name='手机号')),
                ('password', models.CharField(max_length=128, null=True, verbose_name='密码')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='邮箱')),
                ('is_email_verified', models.SmallIntegerField(default=0, verbose_name='邮箱是否已经验证')),
                ('token', models.CharField(max_length=100, null=True, verbose_name='用户令牌')),
                ('status', models.SmallIntegerField(default=0, verbose_name='状态')),
                ('robot', models.SmallIntegerField(default=0, verbose_name='是否为机器人')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=128)),
                ('identity', models.BigIntegerField(verbose_name='唯一标志')),
                ('pid', models.BigIntegerField(null=True, verbose_name='父级identity')),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('assets', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='资产')),
                ('user', models.OneToOneField(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asset', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('relation_id', models.IntegerField(verbose_name='关联id')),
                ('module', models.CharField(max_length=20, verbose_name='关联表名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='金额')),
                ('status', models.SmallIntegerField(verbose_name='状态')),
                ('subject', models.CharField(max_length=100, null=True)),
                ('body', models.CharField(max_length=100, null=True)),
                ('order_sn', models.CharField(max_length=50, null=True)),
                ('pay_method', models.SmallIntegerField()),
                ('pay_at', models.IntegerField(null=True)),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=128, verbose_name='分类名称')),
                ('pid', models.IntegerField(null=True, verbose_name='上级分类id')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=128, verbose_name='需求标题')),
                ('number', models.IntegerField(verbose_name='需求数量')),
                ('number_unit', models.CharField(max_length=20, verbose_name='需求数量单位')),
                ('start_time', models.IntegerField(verbose_name='共享开始时间')),
                ('end_time', models.IntegerField(verbose_name='共享结束时间')),
                ('expect_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='期望单价')),
                ('price_unit', models.SmallIntegerField(choices=[(1, '年'), (2, '月'), (3, '天')], verbose_name='年|月|天')),
                ('address', models.CharField(max_length=200, verbose_name='详细地址')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demands', to='api.Category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demand_city', to='api.Area', verbose_name='市')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demand_district', to='api.Area', verbose_name='区')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demand_province', to='api.Area', verbose_name='省')),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demands', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'demand',
            },
        ),
        migrations.CreateModel(
            name='DepositPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='押金总额')),
                ('user', models.OneToOneField(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deposit_pool', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'deposit_pool',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=200, verbose_name='企业名称')),
                ('trade_type', models.IntegerField(verbose_name='行业类别')),
                ('province', models.IntegerField(null=True, verbose_name='省')),
                ('city', models.IntegerField(null=True, verbose_name='市')),
                ('area', models.IntegerField(null=True, verbose_name='区')),
                ('legal_person', models.CharField(max_length=50, verbose_name='法人代表')),
                ('license_num', models.CharField(max_length=50, verbose_name='营业执照编号')),
                ('bank_public_num', models.CharField(max_length=100, verbose_name='对公银行账号')),
                ('bank', models.CharField(max_length=100, verbose_name='开户银行')),
                ('bank_address', models.CharField(max_length=100, verbose_name='开户银行所在地')),
                ('bank_branch_name', models.CharField(max_length=100, verbose_name='开户银行支行名称')),
            ],
            options={
                'db_table': 'enterprise',
            },
        ),
        migrations.CreateModel(
            name='IdentityCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('code', models.CharField(max_length=8, verbose_name='验证码')),
                ('template_code', models.CharField(max_length=32, null=True, verbose_name='短信模板名称')),
                ('expire_at', models.BigIntegerField(verbose_name='过期时间')),
            ],
            options={
                'db_table': 'identity_code',
            },
        ),
        migrations.CreateModel(
            name='IntegralLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('integral', models.IntegerField(verbose_name='积分')),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='integral_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'integral_log',
            },
        ),
        migrations.CreateModel(
            name='OssMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('relation_id', models.IntegerField(verbose_name='关联id')),
                ('module', models.CharField(max_length=20, verbose_name='关联表名')),
                ('bucket', models.CharField(max_length=200, verbose_name='bucket')),
                ('obj', models.CharField(max_length=200, verbose_name='object')),
                ('time_length', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'oss_media',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=128, verbose_name='共享标题')),
                ('stock', models.IntegerField(verbose_name='共享库存')),
                ('stock_unit', models.CharField(max_length=20, verbose_name='库存数量单位')),
                ('start_time', models.IntegerField(verbose_name='共享开始时间')),
                ('end_time', models.IntegerField(verbose_name='共享结束时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('price_unit', models.SmallIntegerField(choices=[(1, '年'), (2, '月'), (3, '天')], verbose_name='年|月|天')),
                ('address', models.CharField(max_length=200, verbose_name='详细地址')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shares', to='api.Category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_city', to='api.Area', verbose_name='市')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_district', to='api.Area', verbose_name='区')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_province', to='api.Area', verbose_name='省')),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shares', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'share',
            },
        ),
        migrations.CreateModel(
            name='ShareImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('url', models.CharField(max_length=200, verbose_name='图片路径')),
                ('share', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_images', to='api.Share')),
            ],
            options={
                'db_table': 'share_image',
            },
        ),
        migrations.CreateModel(
            name='SignLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sign_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sign_log',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.BigIntegerField(default=common.utils.current_timestamp, null=True, verbose_name='创建时间')),
                ('updated_at', models.BigIntegerField(null=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='真实姓名')),
                ('nickname', models.CharField(max_length=100, unique=True, verbose_name='昵称')),
                ('head_pic', models.CharField(max_length=300, null=True, verbose_name='头像')),
                ('sex', models.SmallIntegerField(default=0, verbose_name='性别')),
                ('certified_status', models.SmallIntegerField(default=0, verbose_name='认证状态')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('privacy_setting', models.IntegerField(default=0, verbose_name='隐私设置')),
                ('parent_user_id', models.IntegerField(null=True, verbose_name='邀请人id')),
                ('integral', models.IntegerField(default=0, verbose_name='积分')),
                ('exp', models.IntegerField(default=0, verbose_name='经验')),
                ('signature', models.CharField(max_length=200, null=True, verbose_name='签名')),
                ('background_image', models.CharField(max_length=300, null=True, verbose_name='背景图')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_city', to='api.Area', verbose_name='市')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_district', to='api.Area', verbose_name='区')),
                ('enterprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Enterprise', verbose_name='所属企业')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_province', to='api.Area', verbose_name='省')),
                ('user', models.OneToOneField(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
