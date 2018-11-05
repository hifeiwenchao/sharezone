from django.db import models
from common import utils
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):

    created_at = models.BigIntegerField(default=utils.current_timestamp, null=True, verbose_name='创建时间')
    updated_at = models.BigIntegerField(null=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class ImageModel(BaseModel):

    url = models.CharField(max_length=200, verbose_name='图片路径')

    class Meta:
        abstract = True


class Area(BaseModel):
    name = models.CharField(max_length=128)
    identity = models.BigIntegerField(verbose_name='唯一标志')
    pid = models.BigIntegerField(null=True, verbose_name='父级identity')
    # children = models.ManyToManyField('self', symmetrical=False, related_name='parents')

    class Meta:
        db_table = 'area'


class User(AbstractUser):

    account = models.CharField(max_length=50, unique=True, null=True, verbose_name='账号')
    phone = models.CharField(max_length=20, unique=True, null=True, verbose_name='手机号')
    password = models.CharField(max_length=128, null=True, verbose_name='密码')
    email = models.CharField(max_length=100, null=True, verbose_name='邮箱')
    is_email_verified = models.SmallIntegerField(default=0, verbose_name='邮箱是否已经验证')
    token = models.CharField(max_length=100, null=True, verbose_name='用户令牌')
    status = models.SmallIntegerField(default=0, verbose_name='状态')
    robot = models.SmallIntegerField(default=0, verbose_name='是否为机器人')

    def __str__(self):
        return '<User {phone}>'.format(**dict(phone=self.phone))

    class Meta:
        db_table = 'user'


class Enterprise(BaseModel):

    name = models.CharField(max_length=200, verbose_name='企业名称')
    trade_type = models.IntegerField(verbose_name='行业类别')
    province = models.IntegerField(null=True, verbose_name='省')
    city = models.IntegerField(null=True, verbose_name='市')
    area = models.IntegerField(null=True, verbose_name='区')
    legal_person = models.CharField(max_length=50, verbose_name='法人代表')
    license_num = models.CharField(max_length=50, verbose_name='营业执照编号')
    bank_public_num = models.CharField(max_length=100, verbose_name='对公银行账号')
    bank = models.CharField(max_length=100, verbose_name='开户银行')
    bank_address = models.CharField(max_length=100, verbose_name='开户银行所在地')
    bank_branch_name = models.CharField(max_length=100, verbose_name='开户银行支行名称')

    def __str__(self):
        return '<Enterprise {name}>'.format(**dict(name=self.name))

    class Meta:
        db_table = 'enterprise'


class UserInfo(BaseModel):

    name = models.CharField(max_length=50, null=True, verbose_name='真实姓名')
    nickname = models.CharField(max_length=100, unique=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatar', null=True, verbose_name='头像')
    sex = models.SmallIntegerField(default=0, verbose_name='性别')
    certified_status = models.SmallIntegerField(default=0, verbose_name='认证状态')
    province = models.ForeignKey(Area, related_name='user_province', null=True, on_delete=models.SET_NULL, verbose_name='省')
    city = models.ForeignKey(Area, related_name='user_city', null=True, on_delete=models.SET_NULL, verbose_name='市')
    district = models.ForeignKey(Area, related_name='user_district', null=True, on_delete=models.SET_NULL, verbose_name='区')
    address = models.CharField(max_length=100, verbose_name='地址')
    privacy_setting = models.IntegerField(default=0, verbose_name='隐私设置')
    parent_user_id = models.IntegerField(null=True, verbose_name='邀请人id')
    integral = models.IntegerField(default=0, verbose_name='积分')
    exp = models.IntegerField(default=0, verbose_name='经验')
    signature = models.CharField(max_length=200, null=True, verbose_name='签名')
    background_image = models.CharField(max_length=300, null=True, verbose_name='背景图')

    enterprise = models.ForeignKey(Enterprise, null=True, on_delete=models.SET_NULL, verbose_name='所属企业')
    user = models.OneToOneField(User, null=True, db_column='uid', on_delete=models.SET_NULL, related_name='user_info')

    def __str__(self):
        return '<UserInfo {nickname}>'.format(**dict(nickname=self.nickname))

    class Meta:
        db_table = 'user_info'


class Asset(BaseModel):
    user = models.OneToOneField(User, null=True, db_column='uid', on_delete=models.SET_NULL, related_name='asset')
    assets = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='资产')

    def __str__(self):
        return '<Asset {assets}>'.format(**dict(assets=self.assets))

    class Meta:
        db_table = 'asset'


class DepositPool(BaseModel):
    user = models.OneToOneField(
        User, null=True, db_column='uid', on_delete=models.SET_NULL, related_name='deposit_pool')
    deposit = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='押金总额')

    class Meta:
        db_table = 'deposit_pool'


class Bill(BaseModel):
    user = models.ForeignKey(User, db_column='uid', null=True, on_delete=models.SET_NULL, related_name='bills')
    relation_id = models.IntegerField(verbose_name='关联id')
    module = models.CharField(max_length=20, verbose_name='关联表名')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='金额')
    status = models.SmallIntegerField(verbose_name='状态')
    subject = models.CharField(max_length=100, null=True)
    body = models.CharField(max_length=100, null=True)
    order_sn = models.CharField(max_length=50, null=True)
    pay_method = models.SmallIntegerField()
    pay_at = models.IntegerField(null=True)

    class Meta:
        db_table = 'bill'


class Category(BaseModel):
    name = models.CharField(max_length=128, verbose_name='分类名称')
    pid = models.IntegerField(null=True, verbose_name='上级分类id')

    class Meta:
        db_table = 'category'


class Demand(BaseModel):
    PRICE_UNIT_CHOICES = (
        (1, '年'),
        (2, '月'),
        (3, '天'),
    )

    title = models.CharField(max_length=128, verbose_name='需求标题')
    number = models.IntegerField(verbose_name='需求数量')
    number_unit = models.CharField(max_length=20, verbose_name='需求数量单位')
    start_time = models.IntegerField(verbose_name='共享开始时间')
    end_time = models.IntegerField(verbose_name='共享结束时间')
    expect_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='期望单价')
    price_unit = models.SmallIntegerField(verbose_name='年|月|天', choices=PRICE_UNIT_CHOICES)
    province = models.ForeignKey(
        Area, related_name='demand_province', null=True, on_delete=models.SET_NULL, verbose_name='省')
    city = models.ForeignKey(
        Area, related_name='demand_city', null=True, on_delete=models.SET_NULL, verbose_name='市')
    district = models.ForeignKey(
        Area, related_name='demand_district', null=True, on_delete=models.SET_NULL, verbose_name='区')
    address = models.CharField(max_length=200, verbose_name='详细地址')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    lng = models.DecimalField(null=True, max_digits=22, decimal_places=15, verbose_name='经度')
    lat = models.DecimalField(null=True, max_digits=22, decimal_places=15, verbose_name='纬度')
    geotable_id = models.IntegerField(null=True, verbose_name='百度地图geotable_id')
    poi_id = models.CharField(null=True, unique=True, max_length=128, verbose_name='百度地图poi_id')

    user = models.ForeignKey(User, db_column='uid', null=True, on_delete=models.SET_NULL, related_name='demands')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='demands')

    class Meta:
        db_table = 'demand'


class Share(BaseModel):
    PRICE_UNIT_CHOICES = (
        (1, '年'),
        (2, '月'),
        (3, '天'),
    )
    STATUS_CHOICES = (
        (1, '开启'),
        (-1, '关闭')
    )

    title = models.CharField(max_length=128, verbose_name='共享标题')
    stock = models.IntegerField(verbose_name='共享库存')
    stock_unit = models.CharField(max_length=20, verbose_name='库存数量单位')
    start_time = models.BigIntegerField(verbose_name='共享开始时间')
    end_time = models.BigIntegerField(verbose_name='共享结束时间')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    price_unit = models.SmallIntegerField(verbose_name='年|月|天', choices=PRICE_UNIT_CHOICES)
    province = models.ForeignKey(
        Area, related_name='share_province', null=True, on_delete=models.SET_NULL, verbose_name='省')
    city = models.ForeignKey(
        Area, related_name='share_city', null=True, on_delete=models.SET_NULL, verbose_name='市')
    district = models.ForeignKey(
        Area, related_name='share_district', null=True, on_delete=models.SET_NULL, verbose_name='区')
    address = models.CharField(max_length=200, verbose_name='详细地址')
    deposit = models.DecimalField(verbose_name='押金', default=0.00, max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    status = models.SmallIntegerField(default=1, verbose_name='状态', choices=STATUS_CHOICES)
    geotable_id = models.IntegerField(null=True, verbose_name='百度地图geotable_id')
    poi_id = models.CharField(null=True, unique=True, max_length=128, verbose_name='百度地图poi_id')

    user = models.ForeignKey(User, db_column='uid', null=True, on_delete=models.SET_NULL, related_name='shares')
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL, related_name='shares')

    class Meta:
        db_table = 'share'


class ShareImage(ImageModel):

    share = models.ForeignKey(
        Share, null=True, on_delete=models.SET_NULL, related_name='share_images')

    class Meta:
        db_table = 'share_image'


class OssMedia(BaseModel):
    relation_id = models.IntegerField(verbose_name='关联id')
    module = models.CharField(max_length=20, verbose_name='关联表名')
    bucket = models.CharField(max_length=200, verbose_name='bucket')
    obj = models.CharField(max_length=200, verbose_name='object')
    time_length = models.IntegerField(default=0)

    class Meta:
        db_table = 'oss_media'


class IdentityCode(BaseModel):
    phone = models.CharField(max_length=32, verbose_name='手机号')
    code = models.CharField(max_length=8, verbose_name='验证码')
    template_code = models.CharField(max_length=32, null=True, verbose_name='短信模板名称')
    expire_at = models.BigIntegerField(verbose_name='过期时间')

    class Meta:
        db_table = 'identity_code'


class SignLog(BaseModel):
    user = models.ForeignKey(User, db_column='uid', null=True, on_delete=models.SET_NULL, related_name='sign_logs')

    class Meta:
        db_table = 'sign_log'


class IntegralLog(BaseModel):
    user = models.ForeignKey(User, db_column='uid', null=True, on_delete=models.SET_NULL, related_name='integral_logs')
    integral = models.IntegerField(verbose_name='积分')

    class Meta:
        db_table = 'integral_log'


class Order(BaseModel):
    PAY_METHOD_CHOICES = (
        (1, '微信'),
        (2, '支付宝'),
        (3, '银联'),
        (4, '钱包'),
    )
    PAY_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '已支付'),
        (3, '支付失败'),
    )

    share = models.ForeignKey(Share, null=True, on_delete=models.SET_NULL, verbose_name='共享商品')
    buyer = models.ForeignKey(User, db_column='buyer_id', on_delete=models.CASCADE, related_name='buyer_order')
    seller = models.ForeignKey(User, db_column='seller_id', on_delete=models.CASCADE, related_name='seller_order')
    order_no = models.CharField(max_length=128, verbose_name='订单号')
    trade_no = models.CharField(max_length=128, verbose_name='交易号')
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=128)
    pay_method = models.SmallIntegerField(verbose_name='支付方式', null=True, choices=PAY_METHOD_CHOICES)
    payment_price = models.DecimalField(
        max_digits=10, null=True, decimal_places=2, verbose_name='实际付款金额，用户实际需要付款的金额，包含了押金池抵扣金额')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单支付金额,不包含押金池抵扣金额')
    pay_status = models.SmallIntegerField(verbose_name='支付状态', default=1, choices=PAY_STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='实际支付金额，支付回调后写入')
    pay_at = models.BigIntegerField(verbose_name='支付时间时间戳', null=True)

    class Meta:
        db_table = 'order'


class OrderInfo(BaseModel):
    STATUS_CHOICES = (
        (1, '待付款'),
        (2, '待发货'),
        (3, '已发货'),
        (4, '待买家评价'),
        (5, '待卖家评价'),
        (6, '已关闭'),
        (7, '双方已评价'),
        (8, '待归还'),
        (9, '归还中'),
    )
    TRADE_METHOD_CHOICES = (
        (1, '买家自提'),
    )
    RENT_UNIT_CHOICES = (
        (1, '年'),
        (2, '月'),
        (3, '天'),
    )
    IS_USE_POOL_CHOICES = (
        (1, '使用押金池'),
        (2, '不使用押金池')
    )
    order = models.OneToOneField(Order, null=True, related_name='order_info', on_delete=models.SET_NULL, verbose_name='订单')
    number = models.IntegerField(verbose_name='数量', default=1)
    message = models.CharField(max_length=256, null=True, verbose_name='买家留言')
    status = models.SmallIntegerField(verbose_name='订单状态', default=1, choices=STATUS_CHOICES)
    trade_method = models.SmallIntegerField(verbose_name='交易方式', choices=TRADE_METHOD_CHOICES)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='租金')
    # rent_unit = models.SmallIntegerField(verbose_name='租金时间单位', choices=RENT_UNIT_CHOICES)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='押金')
    is_use_pool = models.BooleanField(verbose_name='是否使用押金池', default=False, choices=IS_USE_POOL_CHOICES)
    used_pool_deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='押金池中所使用的押金', default=0)
    start_at = models.BigIntegerField(null=True, verbose_name='开始时间')
    end_at = models.BigIntegerField(null=True, verbose_name='结束时间')
    delivery_at = models.BigIntegerField(null=True, verbose_name='发货时间')
    receipt_at = models.BigIntegerField(null=True, verbose_name='收货时间')
    return_at = models.BigIntegerField(null=True, verbose_name='归还时间')

    class Meta:
        db_table = 'order_info'
