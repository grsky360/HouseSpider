import json
from http import cookiejar
from urllib import parse, request


class Ziroom:

    login_url = 'http://passport.ziroom.com/api/index.php?r=user/login'
    fav_url = 'http://i.ziroom.com/index.php?uri=collect/myCollect'
    base_url = 'http://www.ziroom.com/z/vh/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.87 Safari/537.36',
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__login()

    def __login(self):
        post_data = parse.urlencode({
            'phone': self.username,
            'password': self.password,
            'imgVValue': '',
            'seven': 0
        }).encode('utf-8')
        self.cookie_jar = cookiejar.CookieJar()
        self.opener = request.build_opener(request.HTTPCookieProcessor(self.cookie_jar))
        req = request.Request(self.login_url, post_data, self.headers)
        self.opener.open(req)

    def fav(self):
        data_list = []
        self.__fav(1, data_list)
        room_list = []
        for data in data_list:
            room_list.append(self.base_url + data['house_id'] + '.html')
        return room_list

    def __fav(self, page, list):
        post_data = parse.urlencode({
            'pg': page
        }).encode('utf-8')
        req = request.Request(self.fav_url, post_data, self.headers)
        response = self.opener.open(req)
        result = json.loads(response.read().decode('utf-8'))
        total_page = result['total']
        data = result['data']
        list.extend(data.values())
        if page == total_page:
            return list
        self.__fav(page + 1, list)
