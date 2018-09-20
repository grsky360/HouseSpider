import re

from . import core


def lianjia(url):
    soup = core.url_get(url)
    room_name = core.sub_str(soup.find(class_='title-wrapper').find('h1', class_='main').text)
    detail = soup.find(class_='zf-content').find(class_='zf-room').find_all('p')
    location = core.sub_str(detail[6].text.replace('位置：', '')) + ' ' + core.sub_str(detail[5].find('a').text)
    prise = float(core.sub_str(soup.find(class_='zf-content').find(class_='price').find(class_='total').text))
    first_prise = prise * 1.05 * (1 + 1.2)
    total_prise = prise * 1.05 * (12 + 1.2)
    size = core.sub_str(detail[0].text.replace('面积：', '').replace('平米', ''))
    info = core.sub_str(detail[1].text.replace('房屋户型：', '')).split(' ')
    tingshi = info[0]
    get_type = info[1]
    chaoxiang = core.sub_str(detail[3].text.replace('房屋朝向：', ''))
    fs = core.sub_str(detail[2].text.replace('楼层', '').replace('(', '').replace(')', '').replace('：', '').replace('共', '')).split(' ')
    floor = fs[0]
    total_floor = fs[1]
    url = url
    desc = core.sub_str(detail[5].text.replace('小区：', ''))

    start_location = core.get_location(core.sub_str(detail[5].find('a').text))
    to_ziroom = core.to_ziroom(start_location)
    to_tiger = core.to_tiger(start_location)

    return core.model_pack(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type,
                           floor, total_floor, url, desc, to_ziroom, to_tiger)
