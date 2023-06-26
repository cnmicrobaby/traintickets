# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-10 23:03
# @File: station.py

import re

import requests
import urllib3


# 查询12306网站各城市站点对应信息
def get_stations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9261'
    urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    station = re.findall('([\u4e00-\u9fa5]+)\\|([A-Z]+)', response.text)
    stations = dict(station)
    return stations


# 根据站点代码查询站点名称
def get_name(sts, code):
    names = list(sts.keys())
    codes = list(sts.values())
    return names[codes.index(code)]


# 根据站点名称查询站点代码
def get_code(sts, name):
    names = list(sts.keys())
    codes = list(sts.values())
    return codes[names.index(name)]
