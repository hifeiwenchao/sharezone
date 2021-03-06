# 签到增加积分
SIGN_IN_INTEGRAL = 5


class SmsTemplateCode:
    # 注册模板
    REGISTER = 'SMS_143868233'
    # 找回密码
    FIND_PWD = 'SMS_113445084'
    # 重置密码
    RESET_PWD = 'SMS_136389487'
    # 修改手机号
    MODIFY_PHONE = 'SMS_125116069'
    # 绑定手机号
    BIND_PHONE = 'SMS_125026274'
    # 发货
    DELIVERY = 'SMS_130830624'
    # 确认收货
    CONFIRM_RECEIPT = 'SMS_130835764'
    # 余额提现
    BALANCE_PUT_FORWARD = 'SMS_136386972'
    # 共享押金提现
    DEPOSIT_PUT_FORWARD = 'SMS_136399400'
    # 短信登录
    LOGIN = 'SMS_143705422'


class SmsExpire:
    # 注册模板
    REGISTER = 60 * 30 * 1000
    # 找回密码
    FIND_PWD = 60 * 30 * 1000
    # 重置密码
    RESET_PWD = 60 * 30 * 1000
    # 修改手机号
    MODIFY_PHONE = 60 * 30 * 1000
    # 绑定手机号
    BIND_PHONE = 60 * 30 * 1000
    # 发货
    DELIVERY = 60 * 30 * 1000
    # 确认收货
    CONFIRM_RECEIPT = 60 * 30 * 1000
    # 余额提现
    BALANCE_PUT_FORWARD = 60 * 30 * 1000
    # 共享押金提现
    DEPOSIT_PUT_FORWARD = 60 * 30 * 1000
    # 短信登录
    LOGIN = 60 * 30 * 1000


class GeoTableId:
    DEMAND = 1000004772
    SHARE = 1000004885


class OrderStatus:
    # 待支付
    WAIT_PAY = 1
    WAIT_DELIVERY = 2
    SHIPPED = 3
    WAIT_BUYER_COMMENT = 4
    WAIT_SELLER_COMMENT = 5
    CLOSED = 6
    BOTH_COMMENT = 7
    WAIT_RETURN = 8
    RETURNNING = 9


class PayMethod:
    # 支付宝
    ALI_PAY = 1
    # 微信支付
    WECHAT_PAY = 2
    # 银联支付
    UNION_PAY = 3


class ShareStatus:
    # 开启
    OPEN = 1
    # 关闭
    CLOSED = -1



