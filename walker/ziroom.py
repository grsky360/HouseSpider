import re

from . import core


def ziroom(url):
    soup = core.url_get(url)
    room_name = soup.find(class_='room_name').find('h2').text.strip()
    location = re.sub(r'[ \n]{2,}', ' ', soup.find(class_='room_name').find(class_='ellipsis').text.strip())
    prise = float(soup.find(class_='room_price').text.strip().replace('￥', ''))
    first_prise = prise * 1.05 * (1 + 0.96)
    total_prise = prise * 1.05 * (12 + 0.96 - 1.5)
    detail = soup.find(class_='detail_room').find_all('li')
    size = re.sub(r'[ \n]+', '', detail[0].text.strip().replace('面积：', '').replace('㎡', ''))
    chaoxiang = re.sub(r'[ \n]+', '', detail[1].text.strip().replace('朝向：', ''))
    tingshi = re.sub(r'[ \n整合]+', '', detail[2].text.strip().replace('户型：', ''))
    get_type_from = detail[2].find('span', class_='icons').text
    if get_type_from.find('整') != -1:
        get_type = '整租'
    elif get_type_from.find('合') != -1:
        get_type = '合租'
    else:
        get_type = 'error'
    fs = re.sub(r'[ \n]+', '', detail[3].text.strip().replace('楼层：', '').replace('层', '')).split('/')
    floor = fs[0]
    total_floor = fs[1]
    desc = core.sub_str(soup.find(class_='room_tags').text)

    start_position = [soup.find(id='mapsearchText').attrs['data-lng'], soup.find(id='mapsearchText').attrs['data-lat']]
    print(start_position)
    to_ziroom = core.to_ziroom(start_position)
    to_tiger = core.to_tiger(start_position)

    return core.model_pack(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type,
                           floor, total_floor, url, desc, to_ziroom, to_tiger)
