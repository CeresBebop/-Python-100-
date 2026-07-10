#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 百钱百鸡

if __name__ == "__main__":
    # 外层循环控制公鸡数量取值范围为 0~20 (range不包含21)
    for cock in range(0, 21):
        # 内层循环控制母鸡数量取值范围为 0~33 (range不包含34)
        for hen in range(0, 34):
            
            # 根据数学关系，小鸡的数量直接用总数 100 减去公鸡和母鸡的数量
            chicken = 100 - cock - hen
            
            # 约束条件：
            # 1. chicken % 3 == 0 确保小鸡数量能被 3 整除，省去不必要的浮点数计算
            # 2. 5 * cock + 3 * hen + chicken // 3 == 100 确保总花费正好等于 100 元
            if (chicken % 3 == 0) and (5 * cock + 3 * hen + chicken // 3 == 100):
                print("cock = %2d, hen = %2d, chicken = %2d\n" % (cock, hen, chicken))