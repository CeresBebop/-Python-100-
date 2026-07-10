#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 冒泡排序

def bubbleSort(a):
    # 首先获取列表list的总长度，为之后循环比较做准备
    n = len(a)
    # 进行n-1次比较，控制比较的轮数
    i = 1
    while i <= n - 1:
        # 控制每轮比较的次数
        j = 0
        while j < n - i:  # 使用 < 确保 j+1 不会超出列表范围
            # 交换
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
            j += 1
        
        # 【已修正】缩进 8 个空格，使其属于外层 while 循环
        # 打印每一轮交换后的列表
        print(f"第 {i} 轮排序结果: ", end="")
        for a1 in a:
            print(a1, end=" ")
        print()  # 换行
        
        i += 1

if __name__ == "__main__":
    print("请为列表元素赋初值，列表末尾不能有空格（例如: 5 3 9 6 8 2 7）：")
    x = input()
    a = x.split(" ")                                     # 以空格方式分割每个元素
    for i in range(0, len(a)):                           # 输入多个值
        a[i] = int(a[i])
    print("你输入的列表元素为：\n", a)
    print("经过交换后的数组元素为：")
    bubbleSort(a)