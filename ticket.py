# -*- coding:utf-8 -*-
# @Author: microbaby
# @Time: 2023-05-10 23:04
# @File: ticket.py

import requests
from prettytable import PrettyTable
import stations


class TrainsCollection:

    def __init__(self, train_tickets):
        self.train_tickets = train_tickets

    @property
    def plains(self):
        for item in self.train_tickets:
            cm = item.split('|')
            train_no = cm[3]
            from_station = stations.getName(cm[6])
            to_station = stations.getName(cm[7])
            start_time = cm[8]
            arrive_time = cm[9]
            time_duration = cm[10]
            business_seat = cm[32] or '--'
            first_class_seat = cm[31] or '--'
            second_class_seat = cm[30] or '--'
            soft_sleep = cm[23] or '--'
            hard_sleep = cm[28] or '--'
            hard_seat = cm[29] or '--'
            no_seat = cm[26] or '--'
            train_data = [
                train_no,
                '\n'.join([from_station,
                           to_station]),
                '\n'.join([start_time,
                           arrive_time]),
                time_duration,
                business_seat,
                first_class_seat,
                second_class_seat,
                soft_sleep,
                hard_sleep,
                hard_seat,
                no_seat
            ]
            yield train_data

    def pretty_print(self):
        pt = PrettyTable()
        header = '车次 车站 时间 历时 商务座 一等座 二等座 软卧 硬卧 硬座 无座'.split()
        pt.field_names = header
        for train_data in self.plains:
            pt.add_row(train_data)
        pt.align = 'c'
        print(pt.get_string(sortby='时间'))


def getTrainTickets(from_station, to_station, date):
    from_station = stations.getCode(from_station)
    to_station = stations.getCode(to_station)
    url = 'https://kyfw.12306.cn/otn/leftTicket/query'
    params = {
        'leftTicketDTO.train_date': date,
        'leftTicketDTO.from_station': from_station,
        'leftTicketDTO.to_station': to_station,
        'purpose_codes': 'ADULT'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
        'Cookie': '_uab_collina=168372748270487053294913; JSESSIONID=8C3E7C6BA8D658F2F9A176A0C069AA9A; '
                  'BIGipServerotn=1691943178.24610.0000; BIGipServerpassport=803733770.50215.0000; guidesStatus=off; '
                  'highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; '
                  '_jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; '
                  '_jc_save_wfdc_flag=dc; BIGipServerportal=3084124426.17695.0000; _jc_save_toDate=2023-05-11; '
                  'fo=oxuqwudojug3q4xveP9Q7gxnyU3GQXYDFYqAeR8y0B9gFr3N48K_Hyi8yI'
                  '-QPzn6UEVzpC9hAQa_ZRBJ5ysKKLEGgyHr_brj39e7jBQsFBrwMmoZS'
                  '-Tos0nCVK7L68v0u03AMhsWR3eQgA8dlMOZxE8ny60mrX8qTmW0Xi4dFROAchofqEVsrpBC7MY; '
                  '_jc_save_fromDate=2023-05-11'
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    train_tickets = response.json()['data']['result']
    return train_tickets
