#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/30 12:34
# @Author : way
# @Site : 
# @Describe: 10 万厦门招聘数据可视化

from data import SourceDataDemo


class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = 'Twitter data visualization'
        self.counter = {'name': 'Hashtag', 'value':68}
        self.counter2 = {'name': 'user', 'value': 11059}
        self.echart1_data = {
            'title': 'hashtags',
            'data': [
                {"name": "Beijing2022", "value": 237},
                {"name": "Oscars", "value": 11},
                {"name": "OnThisDay", "value": 13},
                {"name": "Olympics", "value": 33},
                {"name": "SuperBowl", "value": 39},
                {"name": "WinterOlympics", "value": 188},
                {"name": "covid", "value": 64},
                {"name": "pandemic", "value": 114},
                {"name": "SharpStick", "value": 22},
                {"name": "TheGildedAge", "value": 74},
                {"name": "TheRequin", "value": 88},

            ]
        }
        self.echart2_data = {
            'title': 'tweet type',
            'data': [
                {"name": "nan", "value": 3249},
                {"name": "retweet", "value": 1135},
                {"name": "original", "value": 1681},
                {"name": "reply", "value": 425},
                {"name": "quote", "value": 9},

            ]
        }
        self.echarts3_data = {
            'title': '工作时间',
            'data': [
                {"name": "6.5小时", "value": 2105},
                {"name": "7小时", "value": 21761},
                {"name": "7.5小时", "value": 41025},
                {"name": "8小时", "value": 104917},
                {"name": "10小时", "value": 4910},
                {"name": "12小时", "value": 3883},
            ]
        }

        self.echart4_data = {
             'title': 'tweet type',
            'data': [
                {"name": "nan", "value": 3249},
                {"name": "retweet", "value": 1135},
                {"name": "original", "value": 1681},
                {"name": "reply", "value": 425},
                {"name": "quote", "value": 9},

            ]
        }
        self.echart5_data = {
            'title': 'hashtags count',
            'data': [
                {"name": "外资", "value": 5412},
                {"name": "民营/私营", "value": 5812},
                {"name": "合资", "value": 5742},
                {"name": "事业单位", "value": 8224},
                {"name": "台资/港资", "value": 5239},
                {"name": "国营企业", "value": 5567},
                {"name": "上市公司", "value": 6432},
                {"name": "其他", "value": 5365},
            ]
        }
