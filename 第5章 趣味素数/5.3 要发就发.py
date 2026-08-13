#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 要发就发 (1898) - 查找不超过 1993 的素数中所有差值为 1898 的素数组合

import math
from typing import List, Tuple


def is_prime(n: int) -> bool:
    """判断一个自然数是否为素数（质数）。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 在 3 到 sqrt(n) 之间按步长 2 遍历奇数因子
    max_factor = int(math.sqrt(n))
    for j in range(3, max_factor + 1, 2):
        if n % j == 0:
            return False
    return True


def fun(i: int) -> int:
    """兼容原代码调用的素数判定函数接口。

    Args:
        i (int): 待检测的数值。

    Returns:
        int: 1 表示素数，0 表示非素数。
    """
    return 1 if is_prime(i) else 0


def find_prime_pairs_with_diff(
    max_limit: int = 1993, diff: int = 1898
) -> List[Tuple[int, int]]:
    """生成不超过 max_limit 的素数序列，并搜索所有差值等于 diff 的素数对。

    Args:
        max_limit (int): 素数上限，默认 1993。
        diff (int): 目标差值，默认 1898。

    Returns:
        List[Tuple[int, int]]: 包含所有符合条件的 (p1, p2) 素数对。
    """
    # 获取不超过 max_limit 的所有素数（包含偶素数 2）
    primes = [num for num in range(2, max_limit + 1) if is_prime(num)]

    prime_set = set(primes)
    results = []

    # 遍历所有素数 p2，检查 p1 = p2 - diff 是否也在素数集合中
    for p2 in primes:
        if p2 > diff:
            p1 = p2 - diff
            if p1 in prime_set:
                results.append((p1, p2))

    return results


def main() -> None:
    """主程序入口：查找并格式化打印所有符合条件的素数组合。"""
    print("列出第一行中差值为1898的所有素数组合: ")

    results = find_prime_pairs_with_diff(max_limit=1993, diff=1898)

    for count, (p1, p2) in enumerate(results, start=1):
        print("(%d). %3d, %d" % (count, p1, p2))


if __name__ == "__main__":
    main()