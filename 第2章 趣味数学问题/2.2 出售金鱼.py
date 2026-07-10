#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 出售金鱼

if __name__ == "__main__":
    flag = 0 # flag作为控制标志
    i = 23
    while flag == 0:
        j = 1 # j表示卖鱼的次数
        x = i # x表示每次卖鱼的条数
        while j <= 4 and x >= 11:
            if (x + 1) % (j + 1) == 0: # 判断x + 1是否能整除j + 1
                x -= (x + 1) // (j + 1)
            else:
                x = 0
                break
            j += 1
        if j == 5 and x == 11:
            print("原来鱼缸中共有%d条金鱼。" % i)
            flag = 1 # 求出结果，flag置为1，退出
        i += 2
