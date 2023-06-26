# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-11 18:04
# @File: main.py

import time
from datetime import datetime

import station as st
import ticket as tk
from log import logger

# 载入各城市车站信息
sts = st.getStations()

if __name__ == '__main__':
    # 判断输入的出发城市信息
    from_station = input('请输入出发城市：')
    while from_station not in list(sts.keys()):
        logger.info('输入的出发城市有误！')
        from_station = input('请输入出发城市：')
    # 判断输入的到达城市信息
    to_station = input('请输入到达城市：')
    while to_station not in list(sts.keys()):
        logger.info('输入的到达城市有误！')
        to_station = input('请输入到达城市：')
    # 判断出发日期信息
    trip_date = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
    while True:
        try:
            date = time.strptime(trip_date, '%Y-%m-%d')
            now_str = datetime.now().strftime('%Y-%m-%d')
            now_date = time.strptime(now_str, '%Y-%m-%d')
            if date.tm_yday < now_date.tm_yday or date.tm_yday > now_date.tm_yday + 14:
                logger.info('输入的日期期限有误！')
                trip_date = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
            else:
                trip_date = time.strftime('%Y-%m-%d', date)
                break
        except Exception as e:
            logger.error(e.args)
            logger.info('输入的日期格式有误！')
            trip_date = input('（格式:2000-01-01，请输入大于等于今天的日期，且不超过15天）\n请输入出发日期：')
    try:
        # 查询火车票信息
        train_tickets = tk.get_train_tickets(from_station, to_station, trip_date)
    except Exception as e:
        logger.error(e.args)
    else:
        # 在控制台输出火车票信息
        train_list = tk.TrainsCollection(train_tickets)
        train_list.pretty_print()
