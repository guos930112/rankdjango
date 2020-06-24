# -*- coding: utf-8 -*-
"""
@Time   ： 2020/6/24 10:55 上午
@Author ： guos
@File   ：test_code.py
@IDE    ：PyCharm

"""
import requests
import json

url_post = 'user_score_update/'
url_get = 'user_score_rank/{}/{}/'
host = 'http://127.0.0.1:8000/'

if __name__ == '__main__':
    # 更新用户分数及排名
    params = {'uid': '5', 'score': 100000}
    res_post = requests.post(url=host + url_post, data=json.dumps(params), headers={'Content-Type': 'application/json'}).text
    print(res_post)
    # 获取排行榜
    res_get = requests.get(url=host + url_get.format(0, 4)).text
    print(res_get)
