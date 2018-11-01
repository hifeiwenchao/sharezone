
from api.models import DepositPool, OrderInfo
from django.db.models import Sum
from api.const import OrderStatus


def create(**kwargs):
    return DepositPool.objects.create(**kwargs)


def using_deposit(user):
    result = OrderInfo.objects.filter(
        order__buyer=user, status__in=[
            OrderStatus.WAIT_DELIVERY, OrderStatus.SHIPPED, OrderStatus.WAIT_RETURN, OrderStatus.RETURNNING
        ]).aggregate(deposit_sum=Sum('deposit'))
    return result['deposit_sum'] or 0
