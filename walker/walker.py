from model import Model
from walker import ziroom, _5i5j, lianjia, xiangyu


def walker(url: str) -> Model:
    if url.find('ziroom.com') >= 0:
        return ziroom.ziroom(url)
    if url.find('bj.5i5j.com') >= 0:
        return _5i5j._5i5j(url)
    if url.find('xiangyu.5i5j.com') >= 0:
        return xiangyu.xiangyu(url)
    if url.find('lianjia.com') >= 0:
        return lianjia.lianjia(url)
    raise RuntimeError
