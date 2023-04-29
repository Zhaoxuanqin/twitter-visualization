#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

class SourceDataDemo:

    def __init__(self):
        # 默认的标题
        self.title = 'Prediction Visualization'
        # 两个小的form看板
        self.counter = {'name': 'Total number of tweets', 'value': 313}
        self.counter2 = {'name': 'total event', 'value': 10}
        # 总共是6个图表，数据格式用json字符串，其中第3个图表是有3个小的图表组成的
        self.echart1_data = {
            'title': 'Sentiment Prediction',
            'data': [
                {"name": "NEGATIVE", "value": 45},
                {"name": "NEGATIVE", "value": 99},
                {"name": "POSITIVE", "value": 170},
                # {"name": "生活服务", "value": 84},
                # {"name": "汽车销售", "value": 99},
                # {"name": "旅游酒店", "value": 37},
                # {"name": "五金建材", "value": 2},
            ]
        }
        self.echart2_data = {
            'title': 'EVENT',
            'data': [
                {"name": "patient centricity", "value": 15},
                {"name": "timely access ", "value": 28},
                {"name": "innovation/innocative therapies", "value": 12},
                {"name": "advocary/reform", "value": 9},
                {"name": "affordability", "value": 13},
                {"name": "health inequity/disparity", "value": 3},
                {"name": "phc", "value": 1},
                {"name": "initiatives/education", "value": 1},
                {"name": "food", "value": 1},
                {"name": "health", "value": 1},
            ]
        }
        self.echarts3_1_data = {
            'title': 'The number of tweets created per day',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车", "value": 4},
                {"name": "旅游", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': 'TIME TENDENCY',
            'data': [
                {"name": "Positive", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4, 6, 5, 2, 3, 2, 5]},
                {"name": "Negative", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8,4, 6, 5, 2, 3, 6, 4]},
                {"name": "Natural", "value": [1, 6, 2, 4, 6, 5, 1, 5, 3, 5, 4, 2, 8, 9, 3, 1, 4, 4, 5, 8, 1, 3, 3,5, 5, 6, 4, 4, 1, 1]},

            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11', '12', '13', '14', '15', '16','17',
                      '18', '19', '20', '21', '22', '23', '24','25','26','27','28','29','30'],
        }
        self.echart5_data = {
            'title': 'Pie chart of predicted results',
            'data': [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ]
        }
        # 这是一个环状图，有颜色的加上没颜色的正好等于100，半径是外圈直径和内圈直径，猜测是左闭右开
        self.echart6_data = {
            'title': 'pie chart of predicted results',
            'data': [
                {"name": "Positive", "value": 170, "value2": 163, "color": "01", "radius": ['59%', '70%']},
                {"name": "Negative", "value": 99, "value2": 214, "color": "05", "radius": ['49%', '60%']},
                {"name": "Natural", "value": 45, "value2": 268, "color": "07", "radius": ['39%', '50%']},
                # {"name": "北京", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                # {"name": "深圳", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        # 这个在哪里用了？？？
        self.map_1_data = {
            'symbolSize': 1000,
            'data': [
                {'name': '海门', 'value': 239},
                {'name': '鄂尔多斯', 'value': 231},
                {'name': '招远', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            # 第一次get获取到的是许多键值对，所以需要对每个键值对再次get
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        # 返回的是标题和对应的数据，并没有说用什么方式展现！
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = 'Data Visualization'

