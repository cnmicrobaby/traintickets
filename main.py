# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-11 18:04
# @File: main.py

import time
from datetime import datetime

import station as st
import ticket as tk
from log import logger

sts = st.getStations()

if __name__ == '__main__':
    fromStation = input('请输入出发城市：')
    while fromStation not in list(sts.keys()):
        logger.info('输入的出发城市有误！')
        fromStation = input('请输入出发城市：')
    toStation = input('请输入到达城市：')
    while toStation not in list(sts.keys()):
        logger.info('输入的到达城市有误！')
        toStation = input('请输入到达城市：')
    tripDate = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
    while True:
        try:
            date = time.strptime(tripDate, '%Y-%m-%d')
            now_str = datetime.now().strftime('%Y-%m-%d')
            now_date = time.strptime(now_str, '%Y-%m-%d')
            if date.tm_yday < now_date.tm_yday or date.tm_yday > now_date.tm_yday + 14:
                logger.info('输入的日期期限有误！')
                tripDate = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
            else:
                tripDate = time.strftime('%Y-%m-%d', date)
                break
        except Exception as e:
            logger.error(e.args)
            logger.info('输入的日期格式有误！')
            tripDate = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
    try:
        traintickets = tk.getTrainTickets(fromStation, toStation, tripDate)
    except Exception as e:
        logger.error(e.args)
    else:
        trainlist = tk.TrainsCollection(traintickets)
        trainlist.pretty_print()
