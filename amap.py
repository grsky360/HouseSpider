# coding: utf-8

import json
from urllib import request, parse


app_key = '77ca7419f73526ec44bc0014d3764a05'
ziroom = [116.499334, 39.973297]
tiger = [116.445434, 39.970480]


def duration(start_position, end_position, city='北京'):
    encoded_city = parse.quote(city)
    url = 'http://restapi.amap.com/v3/direction/transit/integrated?' \
          'key=' + app_key + '&' \
          'origin=' + str(start_position[0]) + ',' + str(start_position[1]) + '&' + \
          'destination=' + str(end_position[0]) + ',' + str(end_position[1]) + '&' + \
          'city=' + encoded_city + '&'
    result = request.urlopen(url).read().decode('utf-8')
    min_duration_bus = 0x7FFFFFFF
    for d in json.loads(result)['route']['transits']:
        min_duration_bus = min(min_duration_bus, float(d['duration']))
    if min_duration_bus == 0x7FFFFFFF:
        min_duration_bus = 0
    min_duration_bus = int(min_duration_bus / 60)

    url = 'http://restapi.amap.com/v3/direction/walking?' \
          'key=' + app_key + '&' \
          'origin=' + str(start_position[0]) + ',' + str(start_position[1]) + '&' + \
          'destination=' + str(end_position[0]) + ',' + str(end_position[1])
    result = request.urlopen(url).read().decode('utf-8')
    min_duration_walk = 0x7FFFFFFF
    for d in json.loads(result)['route']['paths']:
        min_duration_walk = min(min_duration_walk, float(d['duration']))
    if min_duration_walk == 0x7FFFFFFF:
        min_duration_walk = 0
    min_duration_walk = int(min_duration_walk / 60)
    return {
        'bus': str(min_duration_bus),
        'walk': str(min_duration_walk)
    }


def to_ziroom(start_position):
    return duration(start_position, ziroom)


def to_tiger(start_position):
    return duration(start_position, tiger)


def get_location(_place, city='北京'):
    address = parse.quote(_place)
    encoded_city = parse.quote(city)
    url = 'http://restapi.amap.com/v3/geocode/geo?key=' + app_key + '&address=' + address + '&city=' + encoded_city
    result = request.urlopen(url).read().decode('utf-8')
    location = json.loads(result)['geocodes'][0]['location'].split(',')
    return [location[0], location[1]]


if __name__ == '__main__':
    place = '奥林匹克森林公园'
    location = get_location(place)
    _to_tiger = to_tiger(location)
    _to_ziroom = to_ziroom(location)
    print('\t\tbus\t\twalk')
    print('ziroom\t' + _to_ziroom['bus'] + '\t\t' + _to_ziroom['walk'])
    print('tiger\t' + _to_tiger['bus'] + '\t\t' + _to_tiger['walk'])
