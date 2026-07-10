#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 选择排序

def selectionSort(a):
    n = len(a)
    # 外层循环控制排序的轮数，总共需要 n-1 轮
    for i in range(n - 1):
        # 内层循环控制相邻元素的比较和交换
        for j in range(0, n - 1 - i):
            # 如果前一个元素大于后一个元素，则交换位置（将较大的数向后冒泡）
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                
        # 每一轮交换结束后，按格式打印当前列表状态
        print(f"第 {i + 1} 轮排序结果: ", end="")
        for item in a:
            print(item, end=" ")
        print()  # 打印完一轮后换行

if __name__ == "__main__":
    # 更新了输入提示语，与要求保持一致
    print("请为列表元素赋初值，列表末尾不能有空格（例如: 5 3 9 6 8 2 7）：")
    x = input()
    
    # 以空格方式分割每个元素
    a = x.split(" ")
    
    # 将字符串列表转换为整数列表
    for i in range(0, len(a)):
        a[i] = int(a[i])
        
    print("你输入的列表元素为：")
    print(f" {a}")
    print("经过交换后的数组元素为：")
    
    # 调用排序函数
    selectionSort(a)