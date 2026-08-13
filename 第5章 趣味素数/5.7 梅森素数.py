#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 梅森素数（查找指数 i < 20 的所有梅森素数 M(i) = 2^i - 1）

import math


def is_prime(n: int) -> bool:
    """判断一个自然数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    # 修复原代码 Bug：拦截 1 及小于 1 的非素数
    if n <= 1:
        return False
    # 2 是唯一的偶素数
    if n == 2:
        return True
    # 排除大于 2 的偶数
    if n % 2 == 0:
        return False

    # 试除法：仅测试 3 到 sqrt(n) 之间的奇数因子
    max_factor = int(math.sqrt(n))
    i = 3
    while i <= max_factor:
        if n % i == 0:
            return False
        i += 2
    return True


def prime(n: int) -> int:
    """兼容原代码函数名的素数判定接口。

    Args:
        n (int): 待检测的数值。

    Returns:
        int: 是素数返回 1，非素数返回 0。
    """
    return 1 if is_prime(n) else 0


def main() -> None:
    """主程序入口：穷举指数 i < 20，寻找并输出对应的梅森素数 M(i)。"""
    n = 0
    print("梅森素数: ")

    # 遍历指数 i 在区间 [2, 19]
    for i in range(2, 20):
        mp = (2**i) - 1
        # 验证梅森数 M(i) 是否为素数
        if is_prime(mp):
            n += 1
            print(f"M({i}) = {mp}")

    print(f"2的指数n<20的所有梅森素数有: {n}个")


if __name__ == "__main__":
    main()