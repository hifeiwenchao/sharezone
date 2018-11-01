from api.service import dao
from api.utils import map
from api.const import GeoTableId
from django.db import transaction
from api.exceptions.defines import NetWorkException


def publish(user, **kwargs):
    """
    发布共享
    :param user:
    :param kwargs:
    :return:
    """
    with transaction.atomic():
        share = dao.share.create(user=user, **kwargs)
        # 默认地址为上海
        lat = kwargs.get('lat', 31.240164588847)
        lng = kwargs.get('lng', 121.51443399317)
        poi_data = {
            'share_title': kwargs.get('title'),
            'share_id': share.id,
            'share_uid': user.id
        }
        # 创建poi数据
        poi_id = map.create_poi(GeoTableId.SHARE, lat, lng, poi_data)
        if not poi_id:
            raise NetWorkException()
        share.poi_id = poi_id
        share.geotable_id = GeoTableId.SHARE
        share.save()
        return share


def get_shares(**kwargs):
    return dao.share.get_shares(**kwargs)


def get_share(**kwargs):
    return dao.share.get_share(**kwargs)
