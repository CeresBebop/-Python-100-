#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc:牛顿迭代法求方程根

def solution(a, b, c, d):
    x = 1.5
    x0 = 0
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 * x0 + 2 * b * x0 + c
    h = f / fd
    x = x0 - h
    while abs(x - x0) >= 1e-5:
        x0 = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c
        h = f / fd
        x = x0 - h
    
    return x

if __name__ == '__main__':
    print("请输入方程的系数: ")
    # a,b,c,d代表所求方程的系数
    a, b, c, d = map(float, input().split())
    print("方程的参数为: ", a, b, c, d)
    # x用来记录所求得的方程根
    x = solution(a, b, c, d)
    print("方程的根为x=%.6f" % x)


