from api.service import dao
from api.exceptions.defines import NotFoundException, TradeException
from django.db import transaction
from common.utils import generate_order_no
import decimal
from api.utils.alipay import AliPayProxy
from api.const import PayMethod, OrderStatus
import math


def cal_rent(share, number, start_at, end_at):
    """
    计算租金
    :param Share share:
    :param int number:
    :param int start_at:
    :param int end_at:
    :return:
    :rtype: float
    """
    duration = end_at - start_at
    if share.price_unit == 1:
        # 年
        duration = duration / (1000 * 60 * 60 * 24 * 365)
    if share.price_unit == 2:
        # 月
        duration = duration / (1000 * 60 * 60 * 24 * 30)
    if share.price_unit == 3:
        # 日
        duration = duration / (1000 * 60 * 60 * 24)
    return share.price * decimal.Decimal(number * math.ceil(duration))


def gen_order(buyer, share_id, number, start_at, end_at, is_use_pool=True, message=None, trade_method=1):
    """
    提交订单
    :param buyer:
    :param share_id:
    :param number:
    :param start_at:
    :param end_at:
    :param is_use_pool:
    :param message:
    :param trade_method:
    :return:
    """
    share = dao.share.get_share(id=share_id)
    if not share:
        raise NotFoundException('共享商品不存在')
    if share.stock < number:
        raise TradeException('共享商品库存不足')
    if share.start_time > start_at or share.end_time < end_at or \
            share.start_time > end_at or share.end_time < start_at:
        raise TradeException('共享时间超出可提供范围')
    if start_at > end_at:
        raise TradeException('请填写有效的共享时间')
    # 开启事务
    with transaction.atomic():
        # 创建订单
        order_no = generate_order_no()
        # 总共需支付租金
        rent = cal_rent(share, number, start_at, end_at)
        # 正在使用中的押金
        using_deposit = dao.deposit_pool.using_deposit(buyer)
        # 押金池中可用的押金
        usable_deposit = buyer.deposit_pool.deposit - using_deposit
        # 需支付押金
        need_deposit = share.deposit * number
        if usable_deposit >= need_deposit:
            deposit_in_pool = need_deposit
        else:
            deposit_in_pool = usable_deposit
        order = dao.order.create(
            share=share,
            buyer=buyer,
            seller=share.user,
            order_no=order_no,
            subject=share.title,
            body=share.title,
            total_amount=rent + need_deposit - deposit_in_pool,
            price=rent + need_deposit,
        )
        dao.order.create_order_info(
            order=order,
            number=number,
            message=message,
            trade_method=trade_method,
            rent=rent,
            deposit=need_deposit,
            is_use_pool=is_use_pool,
            used_pool_deposit=deposit_in_pool,
            start_at=start_at,
            end_at=end_at,
        )
        return order


def close_order(order_id):
    """
    关闭订单
    :param order_id:
    :return:
    """
    order = dao.order.get_order(id=order_id)
    if order and order.order_info.status == OrderStatus.WAIT_PAY:
        return dao.order.update_status(order_id, OrderStatus.CLOSED)
    raise TradeException('当前无法关闭订单')


def pay(user, order_id, pay_method, is_mobile=True):
    """
    发起第三方支付订单创建请求
    :param user:
    :param order_id:
    :param pay_method:
    :param is_mobile:
    :return:
    """
    order = dao.order.get_order(id=order_id, buyer=user)
    if not order:
        raise NotFoundException('订单不存在')
    if order.order_info.status != OrderStatus.WAIT_PAY:
        raise TradeException('该订单状态不可支付')

    if pay_method == PayMethod.ALI_PAY:
        proxy = AliPayProxy()
        if is_mobile:
            return proxy.trade_app_pay(
                out_trade_no=order.order_no,
                total_amount=float(order.total_amount),
                subject=order.subject,
                body=order.body,
            )
        else:
            return proxy.trade_page_pay(
                out_trade_no=order.order_no,
                total_amount=float(order.total_amount),
                subject=order.subject,
                body=order.body,
            )
    elif pay_method == PayMethod.WECHAT_PAY:
        # todo
        pass
    elif pay_method == PayMethod.UNION_PAY:
        # todo
        pass
    else:
        raise TradeException('暂不支持此交易方式')
