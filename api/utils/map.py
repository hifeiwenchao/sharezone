import requests
from common.utils import config


AK = config('LBS', 'ak')


def geocoder(address, city=None, output='json'):
    """
    http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
    地理编码服务
    用户可通过该功能，将结构化地址（省/市/区/街道/门牌号）解析为对应的位置坐标。地址结构越完整，地址内容越准确，解析的坐标精度越高
    :param address:
    :param city:
    :param output:
    :return:
    """
    data = dict(
        address=address,
        output=output,
        ak=AK
    )
    if city:
        data['city'] = city
    r = requests.post('http://api.map.baidu.com/geocoder/v2/', data=data)
    return r.json()


def reverse_geocoder(lat, lng, pois=0, output='json'):
    """
    http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding-abroad
    逆地理编码服务
    用户可通过该功能，将位置坐标解析成对应的行政区划数据以及周边高权重地标地点分布情况，整体描述坐标所在的位置。
    :param lat:
    :param lng:
    :param pois:
    :param output:
    :return:
    """
    data = dict(
        location=str(lat) + ',' + str(lng),
        pois=pois,
        output=output,
        ak=AK
    )
    r = requests.post('http://api.map.baidu.com/geocoder/v2/', data=data)
    return r.json()


def ip_location(ip=None):
    """
    ip定位
    :param ip:
    :return:
    """
    data = dict(ak=AK)
    if ip:
        data['ip'] = ip
    r = requests.post('http://api.map.baidu.com/location/ip', data=data)
    return r.json()


def create_geotable(name, is_published):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    创建表
    :param name:
    :param is_published:
    :return:
    """
    data = dict(
        name=name,
        is_published=is_published,
        ak=AK
    )
    r = requests.post('http://api.map.baidu.com/geodata/v4/geotable/create', data=data)
    return r.json()


def list_geotables(name=None):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    :param name:
    :return:
    """
    data = dict(ak=AK)
    if name:
        data['name'] = name
    r = requests.post('http://api.map.baidu.com/geodata/v4/geotable/list', data=data)
    return r.json()


def get_geotable_detail(table_id):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    :param table_id:
    :return:
    """
    data = dict(
        id=table_id,
        ak=AK
    )
    r = requests.post('http://api.map.baidu.com/geodata/v4/geotable/detail', data=data)
    return r.json()


def delete_geotable(table_id):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    只有表中数据全部清空后才能删除
    :param table_id:
    :return:
    """
    data = dict(
        id=table_id,
        ak=AK
    )
    r = requests.post('http://api.map.baidu.com/geodata/v4/geotable/delete', data=data)
    return r.json()


def create_column(table_id, name, key, col_type, is_search_field=0, is_index_field=0):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    :param table_id:
    :param name:
    :param key:
    :param col_type:
    :param is_search_field:
    :param is_index_field:
    :return:
    """
    data = dict(
        geotable_id=table_id,
        name=name,
        key=key,
        type=col_type,
        is_search_field=is_search_field,
        is_index_field=is_index_field,
        ak=AK
    )
    r = requests.post('http://api.map.baidu.com/geodata/v4/column/create', data=data)
    return r.json()


def create_poi(table_id, latitude, longitude, data, title=None, address=None, tags=None, coord_type=1):
    """
    http://lbsyun.baidu.com/index.php?title=lbscloud/api/geodataV4
    添加poi数据
    :param table_id:
    :param latitude:
    :param longitude:
    :param data:
    :param title:
    :param address:
    :param tags:
    :param coord_type:
    :return:
    :rtype: str poi_id
    """
    params = dict(
        geotable_id=table_id,
        latitude=latitude,
        longitude=longitude,
        ak=AK
    )
    if title:
        params['title'] = title
    if address:
        params['address'] = address
    if tags:
        params['tags'] = tags
    if coord_type:
        params['coord_type'] = coord_type
    params.update(data)

    r = requests.post('http://api.map.baidu.com/geodata/v4/poi/create', data=params)
    if r.status_code == 200:
        response = r.json()
        if response['status'] == 0:
            return response['id']


if __name__ == '__main__':
    # print(reverse_geocoder(31.240164588847, 121.51443399317))
    # print(geocoder('上海市浦东新区世纪大道100号'))
    # print(ip_location())
    # # print(create_geotable('test1', 1))
    # print(list_geotables())
    # print(get_geotable_detail(1000004771))
    # print(delete_geotable(1000004771))
    # print(create_column(1000004770, 'aoo', 'boo', 1))
    print(create_poi(1000004885, 31.240164588847, 121.51443399317, {'boo': 666}, address='松江区吧'))

