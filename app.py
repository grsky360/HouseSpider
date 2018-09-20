import traceback

import fav.ziroom
import walker.walker as walker
import xlslib


def get_list(pt):
    pt_room_list = []
    if pt == '自如':
        user_list = [
            # {
            #     'username': '',
            #     'password': ''
            # }
        ]
        for user in user_list:
            ziroom = fav.ziroom.Ziroom(user['username'], user['password'])
            pt_room_list.extend(ziroom.fav())
    return pt_room_list


if __name__ == '__main__':
    xls_name = './zhaofang.xls'

    room_list = {
        '我爱我家-相寓': [

        ],
        '我爱我家': [

        ],
        # '自如': get_list('自如'),
        'test': [
            # 'http://www.ziroom.com/z/vr/61310202.html'
        ],
        '链家': [

        ]
    }
    list_error = []
    for pt, sublist in room_list.items():
        for url in sublist:
            try:
                model = walker.walker(url)
                xlslib.write(xls_name, pt, model)
            except:
                traceback.format_exc()
                list_error.append(url)
    print(list_error)
