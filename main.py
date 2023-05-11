# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-11 18:04
# @File: main.py

import ticket

if __name__ == '__main__':
    fromStation = input('请输入出发城市：')
    toStation = input('请输入到达城市：')
    tripDate = input('请输入出发日期（格式:2000-01-01）：')
    traintickets = ticket.getTrainTickets(fromStation, toStation, tripDate)
    trainlist = ticket.TrainsCollection(traintickets)
    trainlist.pretty_print()
