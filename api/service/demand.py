from api.service import dao
from api.utils import map
from api.const import GeoTableId
from django.db import transaction


def publish(user, **kwargs):
    """
    发布需求
    :param user:
    :param kwargs:
    :return:
    """
    with transaction.atomic():
        demand = dao.demand.create(user=user, **kwargs)

        lat = kwargs.get('lat')
        lng = kwargs.get('lng')
        poi_data = {
            'demand_title': kwargs.get('title'),
            'demand_id': demand.id,
            'demand_uid': user.id
        }
        # 1/0
        # 创建poi数据
        poi_id = map.create_poi(GeoTableId.DEMAND, lat, lng, poi_data)
        demand.poi_id = poi_id
        demand.geotable_id = GeoTableId.DEMAND
        demand.save()
        return demand


def get_demands(**kwargs):
    return dao.demand.get_demands(**kwargs)

