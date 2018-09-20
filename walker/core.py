import re
import ssl

from urllib import request

from bs4 import BeautifulSoup

import amap
from model import Model

ssl._create_default_https_context = ssl._create_unverified_context


def url_get(url) -> BeautifulSoup:
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/67.0.3396.87 Safari/537.36')
    data = request.urlopen(req).read().decode('utf-8')
    return BeautifulSoup(data, 'html.parser')


def model_pack(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type, floor,
               total_floor, url, desc='', to_ziroom='', to_tiger='') -> Model:
    return Model(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type, floor,
                 total_floor, url, desc, to_ziroom, to_tiger)


def sub_str(un_done_str):
    un_done_str = re.sub('\r|\n|\\s', ' ', un_done_str)
    un_done_str = re.sub(r'[ ]{2,}', ' ', un_done_str)
    return un_done_str


def to_ziroom(start_position):
    duration = amap.to_ziroom(start_position)
    return 'bus: ' + duration['bus'] + '; walk: ' + duration['walk']


def to_tiger(start_position):
    duration = amap.to_tiger(start_position)
    return 'bus: ' + duration['bus'] + '; walk: ' + duration['walk']


def get_location(position):
    location = amap.get_location(position)
    print(location)
    return location
