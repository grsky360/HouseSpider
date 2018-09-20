# coding: utf-8


class Model:

    def __init__(self, room_name, location, prise, first_prise, total_prise, size, tingshi, chaoxiang, get_type,
                 floor, total_floor, url, desc='', to_ziroom='', to_tiger=''):
        self.room_name = room_name
        self.location = location
        self.prise = prise
        self.first_prise = first_prise
        self.total_prise = total_prise
        self.size = size
        self.tingshi = tingshi
        self.chaoxiang = chaoxiang
        self.floor = floor
        self.total_floor = total_floor
        self.get_type = get_type
        self.url = url
        self.desc = desc
        self.to_ziroom = to_ziroom
        self.to_tiger = to_tiger
