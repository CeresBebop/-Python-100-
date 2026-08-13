#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 回文素数（查找 1000 以内的所有回文素数）

import math


def is_prime(n: int) -> bool:
    """判断一个自然数是否为素数（质数）。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 试除法：遍历 3 到 sqrt(n) 之间的奇数因子
    max_factor = int(math.sqrt(n))
    for i in range(3, max_factor + 1, 2):
        if n % i == 0:
            return False
    return True


def fun(n: int) -> int:
    """兼容原代码函数名的素数判定接口。

    Args:
        n (int): 待判断的数值。

    Returns:
        int: 1 表示素数，0 表示非素数。
    """
    return 1 if is_prime(n) else 0


def is_palindrome(n: int) -> bool:
    """判断一个整数是否为回文数（正读与反读完全相同的数）。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 若为回文数返回 True，否则返回 False。
    """
    s = str(n)
    return s == s[::-1]


def main() -> None:
    """主程序入口：查找并按制表符对齐打印 1000 以内的回文素数。"""
    print("1000以内的回文素数: ")

    count = 0
    # 遍历 2 到 1000 之间的自然数
    for n in range(2, 1000):
        # 同时满足：1. 是回文数；2. 是素数
        if is_palindrome(n) and is_prime(n):
            print(f"{n}\t", end="")
            count += 1
            # 每 10 个数值换一行，保持输出规整
            if count % 10 == 0:
                print()

    # 结尾换行控制
    if count % 10 != 0:
        print()

    print(f"\n共找到 {count} 个回文素数。")


if __name__ == "__main__":
    main()