import re

from . import core


def _5i5j(url):
    matcher = re.match(r'.*/([0-9]+.html)', url)
    url = 'https://m.5i5j.com/bj/zufang/' + matcher.group(1)
    soup = core.url_get(url)
    room_name = core.sub_str(soup.find(class_='huose_mess').find('h1').text)
    location = room_name
    detail = soup.find('ul', class_='house_Dmain').find_all('li')
    prise = float(core.sub_str(detail[0].text.replace('租金', '').replace('元/月', '')))
    ya = int(core.sub_str(detail[1].text.replace('支付', '')[1]))
    fu = int(core.sub_str(detail[1].text.replace('支付', '')[3]))
    first_prise = prise * (ya + fu)
    total_prise = prise * 12
    desc = core.sub_str(detail[1].text.replace('支付', ''))
    size = core.sub_str(detail[2].text.replace('面积', '').replace('㎡', ''))
    tingshi = core.sub_str(detail[3].text.replace('户型', ''))
    if detail[4].text.find('朝向') != -1:
        chaoxiang = core.sub_str(detail[4].text.replace('朝向', ''))
        get_type = core.sub_str(detail[7].text.replace('出租方式', ''))
        fs = core.sub_str(detail[5].text.replace('楼层', '')).split('/')
        floor = fs[0]
        total_floor = fs[1]
    else:
        chaoxiang = ''
        get_type = core.sub_str(detail[6].text.replace('出租方式', ''))
        fs = core.sub_str(detail[4].text.replace('楼层', '')).split('/')
        floor = fs[0]
        total_floor = fs[1]

    position = core.sub_str(soup.find(class_='moduleMap_box').find('p').text.replace('地址：', ''))
    start_position = core.get_location(position)
    to_ziroom = core.to_ziroom(start_position)
    to_tiger = core.to_tiger(start_position)
    return core.model_pack(room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type,
                           floor, total_floor, url, desc, to_ziroom, to_tiger)
