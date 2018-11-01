from api.service import dao
from api.exceptions.defines import NotFoundException, TradeException
from django.db import transaction
from common.utils import generate_order_no
import decimal


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
        duration = duration / (60 * 60 * 24 * 365)
    if share.price_unit == 2:
        # 月
        duration = duration / (60 * 60 * 24 * 30)
    if share.price_unit == 3:
        # 日
        duration = duration / (60 * 60 * 24)
    return share.price * decimal.Decimal(number * duration)


def gen_order(buyer, share_id, number, start_at, end_at, is_use_pool=True, message=None, trade_method=1):
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
            payment_price=rent + need_deposit - deposit_in_pool,
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


