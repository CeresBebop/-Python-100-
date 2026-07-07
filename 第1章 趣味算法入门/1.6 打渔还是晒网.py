#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 打渔还是晒网

# 判断是否为闰年。是，则返回1；否，则返回0
def runYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # 是闰年
        return 1
    else:
        return 0

# 计算指定日期距离1990年1月1日的天数
def countDay(currentday):
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    totalDay = 0
    year = 1990
    while year < currentday['year']: # 求出指定日期之前的每一年的天数之和
        if runYear(year) == 1: # 判断是否为闰年
            totalDay += 366
        else:
            totalDay += 365

        year += 1

    # 如果为闰年，则二月份为29天
    if runYear(currentday['year']) == 1:
        perMonth[2] += 1

    i = 0
    while i < currentday['month']:
        totalDay += perMonth[i]
        i += 1

    totalDay += currentday['day']

    return totalDay

if __name__ == "__main__":
    while True:
        print("Please input 指定日期 包括年，月，日 如： 1999 1 31")
        year, month, day = [int(i) for i in input().split()]
        # 定义一个日期字典
        today = {'year': year, 'month': month, 'day': day}
        
        totalDay = countDay(today) # 求出指定日期距离1990年1月1日的天数
        print("%d年%d月%d日距离1990年1月1日相差 %d 天" % (year, month, day, totalDay))

        # 天数 % 5， 判断输出打渔还是晒网
        result = totalDay % 5
        if result > 0 and result < 4:
            print("今天是打渔的日子")
        else:
            print("今天是晒网的日子")
