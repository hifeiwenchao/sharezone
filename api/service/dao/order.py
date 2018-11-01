from api.models import Order, OrderInfo


def create(**kwargs):
    return Order.objects.create(**kwargs)


def get_order(**kwargs):
    return Order.objects.filter(**kwargs).first()


def get_orders(**kwargs):
    return Order.objects.filter(**kwargs)


def create_order_info(**kwargs):
    return OrderInfo.objects.create(**kwargs)

