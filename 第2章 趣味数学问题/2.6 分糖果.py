#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 经典分糖果算法（支持动态人数扩展）

from typing import List

def judge(candy: List[int]) -> bool:
    """判断所有孩子手中的糖果数是否不同。

    使用 Python 集合(set)去重特性进行高效判断。
    
    Args:
        candy (List[int]): 存储每个孩子糖果数量的列表。

    Returns:
        bool: 若糖果数不完全相同返回 True（对应原版 1），否则返回 False（对应原版 0）。
    """
    if not candy:
        return False
    return len(set(candy)) > 1


def printResult(s: List[int], j: int) -> None:
    """输出当前轮次及每个孩子手中的糖果数量。

    Args:
        s (List[int]): 当前每个孩子的糖果数量列表。
        j (int): 当前的分糖轮次。
    """
    # 格式化输出轮次，保留 4 个字符宽度
    print(f"{j:4d}", end=" ")
    # 格式化输出每个孩子的糖果数
    for count in s:
        print(f"{count:4d}", end=" ")
    print()


def giveSweets(sweet: List[int], j: int) -> None:
    """执行分糖果的核心逻辑，直至所有孩子手中的糖果数量相等。

    Args:
        sweet (List[int]): 初始分配的糖果数列表。
        j (int): 初始轮次计数。
    """
    num_children = len(sweet)
    if num_children <= 1:
        return

    # 动态创建与孩子数量相等的临时列表，用于暂存每轮分出去的糖果数
    t = [0] * num_children

    # 若糖果数量不完全相同，则继续循环
    while judge(sweet):
        # 1. 每个孩子先将自己手中的糖果平分，奇数者向老师额外多要 1 块后再平分
        for i in range(num_children):
            if sweet[i] % 2 != 0:
                # 奇数则加 1 补为偶数
                sweet[i] += 1
            # 平分自己手中的糖果
            sweet[i] //= 2
            # 记录准备分给右边孩子的那一半糖果
            t[i] = sweet[i]

        # 2. 将分出来的一半糖果传给右边相邻的孩子（形成环形传递）
        # 孩子 1 到 n-1 分别接收左边孩子的糖果
        for n in range(num_children - 1):
            sweet[n + 1] += t[n]
        # 孩子 0 接收最后一个孩子传来的糖果，完成闭环
        sweet[0] += t[-1]

        j += 1
        printResult(sweet, j)


if __name__ == "__main__":
    # 定义初始分配给每个孩子的糖果数列表（支持任意长度）
    sweet_data = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
    
    # 动态生成表头，完美适应不同数量的孩子
    print("child", end="")
    for idx in range(len(sweet_data)):
        print(f"{idx + 1:4d}", end=" ")
    print()
    
    # 打印对齐的分隔线
    print("." * (5 + len(sweet_data) * 5))
    print("次数   糖果数")
    
    # 打印初始状态（第 0 轮）
    initial_round = 0
    printResult(sweet_data, initial_round)
    
    # 执行分糖果算法
    giveSweets(sweet_data, initial_round)