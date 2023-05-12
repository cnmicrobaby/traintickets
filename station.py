# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-10 23:03
# @File: station.py

import re

import requests
import urllib3


def getStations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9261'
    urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    station = re.findall('([\u4e00-\u9fa5]+)\\|([A-Z]+)', response.text)
    stations = dict(station)
    return stations


def getName(sts, code):
    names = list(sts.keys())
    codes = list(sts.values())
    return names[codes.index(code)]


def getCode(sts, name):
    names = list(sts.keys())
    codes = list(sts.values())
    return codes[names.index(name)]
