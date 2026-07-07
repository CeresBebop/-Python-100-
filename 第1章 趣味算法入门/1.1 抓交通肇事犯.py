#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc:抓交通肇事犯

if __name__ == '__main__':
    # i代表前两位车牌号数字， j代表后两位车牌号数字，k代表车牌号
    for i in range(10):
        for j in range(10): # 穷举前两位和后两位车牌数字
            # 判断前两位和后两位数字是否相同
            if i != j:
                # 组成四位车牌号码
                k = 1000 * i + 100 * i + 10 * j + j
                # 判断k是否是某个数的平方，是就输出
                for temp in range(31, 100):
                    if temp * temp  == k:
                        print("车牌号为： ", k)