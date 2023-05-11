# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-10 23:03
# @File: stations.py

import re
import requests
import urllib3

urllib3.disable_warnings()
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9261'
response = requests.get(url, verify=False)
station = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
stations = dict(station)
names = list(stations.keys())
codes = list(stations.values())


def getName(code):
    return names[codes.index(code)]


def getCode(name):
    return codes[names.index(name)]
