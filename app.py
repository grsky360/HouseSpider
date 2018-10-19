# coding:utf-8
import traceback
import threading

from config import config
import fav.ziroom
import walker.walker as walker
import xlslib


def get_list(pt):
    pt_room_list = []
    if pt == '自如':
        user_list = config.configs['users']['ziroom']
        for user in user_list:
            ziroom = fav.ziroom.Ziroom(user['username'], user['password'])
            pt_room_list.extend(ziroom.fav())
    return pt_room_list


def process(url, models, list_error):
    try:
        model = walker.walker(url)
        models.append(model)
    except():
        traceback.format_exc()
        list_error.append(url)


if __name__ == '__main__':
    xls_name = './zhaofang.xls'

    room_list = {
        '我爱我家-相寓': [

        ],
        '我爱我家': [

        ],
        '自如': get_list('自如'),
        'test': [

        ],
        '链家': [

        ]
    }
    list_error = []
    for pt, sublist in room_list.items():
        threads = []
        models = []
        for url in sublist:
            t = threading.Thread(target=process, args=(url, models, list_error))
            threads.append(t)
        for th in threads:
            if not th.is_alive():
                th.start()
        for thj in threads:
            thj.join()
        for model in models:
            xlslib.write(xls_name, pt, model)
    print(list_error)
