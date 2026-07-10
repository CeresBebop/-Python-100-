#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 求车速（使用 while 循环）

if __name__ == "__main__":
    a = [0, 0, 0, 0, 0] # 列表a用来存放分解后的5个数字
    
    # 1. 初始化外层 while 循环变量 i
    i = 95860 
    
    # 相当于原来的 for i in range(95860, 100000)
    while i < 100000:
        t = 0
        k = 100000
        
        # 内层循环：分解当前 i 的 5 位数
        while k >= 10:
            # 注意：Python 3 中 k / 10 会变成浮点数，这里改用 // 确保是整数，避免索引或计算出错
            a[t] = int((i % k) // (k // 10)) 
            k //= 10  # 同样改为整除 //
            t += 1
            
        # 判断是否为对称数（回文数）
        if a[0] == a[4] and a[1] == a[3]:
            print("里程表上出现的新的对称数为: %d%d%d%d%d" % (a[0], a[1], a[2], a[3], a[4]))
            print("该车的速度为: %.2f" % ((i - 95859) / 2.0))
            break # 找到符合条件的第一个数后跳出外层 while 循环
            
        # 2. 每次循环结束，i 自增 1
        i += 1