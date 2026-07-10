#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc:兔子产子

if __name__ == '__main__':
    fib1 = 1
    fib2 = 1
    i = 3
    # 输出第一个月和第二个月的兔子对数
    print("%6d      %6d" %(fib1, fib2), end="       ")
    while i <= 30:
        fib = fib1 + fib2 # 迭代求出当前月的兔子对数
        print("%6d" %fib, end="       ") # 输出当前月的兔子对数
        if i % 4 == 0: 
            print() # 每输出四个月的兔子对数就换行
        fib2 = fib1 # 为下一次的迭代做准备
        fib1 = fib # 求出新的fib1
        i += 1