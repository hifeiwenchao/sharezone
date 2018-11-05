from api.models import Order, OrderInfo


def create(**kwargs):
    return Order.objects.create(**kwargs)


def get_order(**kwargs):
    return Order.objects.filter(**kwargs).first()


def get_orders(**kwargs):
    return Order.objects.filter(**kwargs)


def create_order_info(**kwargs):
    return OrderInfo.objects.create(**kwargs)


def get_order_by_user(user, **kwargs):
    return Order.objects.filter(buyer=user, **kwargs).first()


def update_status(order_id, status):
    return OrderInfo.objects.filter(order_id=order_id).update(status=status)
