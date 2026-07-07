#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 百钱百鸡

if __name__ == "__main__":
    # 使用 for 循环自动控制范围，省心又安全
    for cock in range(0, 21):          # 公鸡最多20只 (range不包含21)
        for hen in range(0, 34):       # 母鸡最多33只
            for chicken in range(0, 101):  # 小鸡最多100只
                
                # 条件控制：钱数凑够100，只数凑够100
                if (5 * cock + 3 * hen + chicken / 3.0 == 100) and (cock + hen + chicken == 100):
                    print("cock = %2d, hen = %2d, chicken = %2d\n" % (cock, hen, chicken))