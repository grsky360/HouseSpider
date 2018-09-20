import re

from . import core


def xiangyu(url):
    soup = core.url_get(url)
    room_name = core.sub_str(soup.find(class_='css-title').find('span').text)
    prise = float(core.sub_str(soup.find(id='showPrice').text))
    first_prise = prise * (1 + 5.8 / 100) * (1 + 1)
    total_prise = prise * (1 + 5.8 / 100) * 12
    uls = soup.find(class_='main-right-list').find_all('ul')
    ds1 = uls[0].find_all('li')
    ds2 = uls[1].find_all('li')
    tingshi = core.sub_str(ds1[0].text.replace('户型：', ''))
    location = core.sub_str(ds2[2].text.replace('位置：', ''))
    size = core.sub_str(ds1[1].text.replace('面积：', '').replace('㎡', ''))
    chaoxiang = ''
    if ds2[3].text.find('朝向') != -1:
        chaoxiang = core.sub_str(ds2[3].text.replace('朝向：', ''))
    get_type = core.sub_str(ds2[0].text.replace('方式：', ''))
    fs = core.sub_str(ds2[1].text.replace('楼层：', '').replace('共', '')).split('/')
    floor = fs[0]
    total_floor = fs[1]
    url = url
    desc = ''

    start_location = core.get_location(room_name.split(' ')[0])
    to_ziroom = core.to_ziroom(start_location)
    to_tiger = core.to_tiger(start_location)
    return core.model_pack(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type,
                           floor, total_floor, url, desc, to_ziroom, to_tiger)
