#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 折半查找


if __name__ == "__main__":
   a =  [-3, 4, 7, 9, 13, 45, 67, 89, 180]
   low = 0 # 数组上界
   high = len(a) - 1 # 数组下界
   k = -1 # 记录
   print("a数组中的数据如下: ")
   for i in a:
       print(i, end=" ") # 输出数组中原数据数列
   print()
   m = int(input("Enter m = : ")) # 变量m为要查找的整数
   while low <= high: # 继续查找的控制条件
       mid = (low + high) // 2 # 变量mid为数组序列的中间位置
       if m < a[mid]:
             high = mid - 1
       else:
            if m > a[mid]:
               low = mid + 1
            else:
               k = mid
               break # 一旦找到所要查找的元素便退出循环
   if k >= 0:
      print("m = %d, index = %d" % (m, k))
   else:
      print("Not be found!")