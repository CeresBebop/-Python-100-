#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 完数 (Perfect Numbers)

def sum_of_proper_divisors(num: int) -> int:
    """计算一个正整数的所有真因子（除了自身以外的因数）之和。

    优化算法：将时间复杂度从原代码的 O(num) 降低至 O(sqrt(num))。
    利用因数成对出现的特性，只需遍历到该数的平方根，大幅减少在大数据量下的运算耗时。

    Args:
        num (int): 待计算的整数。

    Returns:
        int: 所有真因子之和。
    """
    if num <= 1:
        return 0
    total = 1  # 1 必定是任意大于 1 的正整数的真因子
    
    # 只需要循环到该数的平方根
    limit = int(num ** 0.5)
    for j in range(2, limit + 1):
        if num % j == 0:
            total += j
            other_divisor = num // j
            if other_divisor != j:  # 避免对完全平方数（如 4, 9, 16 等）重复累加相同的平方根
                total += other_divisor
    return total


def find_perfect_numbers(limit: int) -> list[int]:
    """在指定范围内寻找所有的完数。

    Args:
        limit (int): 检索范围的上限。

    Returns:
        list[int]: 找到的完数列表。
    """
    perfect_numbers = []
    for i in range(2, limit + 1):
        if sum_of_proper_divisors(i) == i:
            perfect_numbers.append(i)
    return perfect_numbers


def main() -> None:
    """主入口函数，获取用户输入上限并检索打印完数。"""
    try:
        user_input = input("请输入所选范围上限（回车默认 1000）：").strip()
        # 提供默认参数 1000 确保一键运行时即便直接回车也不会引发报错
        n = int(user_input) if user_input else 1000
        
        if n < 2:
            print("输入错误：上限必须不小于 2")
            return

        perfect_nums = find_perfect_numbers(n)
        
        if perfect_nums:
            print(f"\n2到{n}之间的完数有：")
            for num in perfect_nums:
                print(f"- {num}")
        else:
            print(f"\n2到{n}之间未找到完数。")

    except ValueError:
        print("输入错误：请输入有效的整数")


if __name__ == "__main__":
    main()