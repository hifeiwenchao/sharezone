from api.service import dao
from api.utils import map
from api.const import GeoTableId


def publish(user, **kwargs):
    demand = dao.demand.create(user=user, **kwargs)

    lat = kwargs.get('lat')
    lng = kwargs.get('lng')
    poi_data = {
        'demand_title': kwargs.get('title'),
        'demand_id': demand.id,
        'demand_uid': user.id
    }
    map.create_poi(GeoTableId.DEMAND, lat, lng, poi_data)
    return demand


