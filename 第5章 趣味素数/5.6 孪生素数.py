#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 孪生素数（寻找 3 到 1000 之间的所有孪生素数对）

import math


def prime(n: int) -> int:
    """判断一个自然数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

    Returns:
        int: 若为素数返回 1，否则返回 0。
    """
    # 拦截小于 2 的非素数
    if n <= 1:
        return 0
    # 2 是唯一的偶素数
    if n == 2:
        return 1
    # 排除大于 2 的偶数
    if n % 2 == 0:
        return 0

    # 试除法：只测试 3 到 sqrt(n) 之间的奇数
    k = int(math.sqrt(n))
    i = 3
    while i <= k:
        if n % i == 0:
            return 0
        i += 2
    return 1


def main() -> None:
    """主程序入口：查找并格式化打印 3 到 1000 之间的孪生素数对。"""
    count = 0
    print("3到1000之间的孪生素数: ")

    # 遍历区间 [3, 998]，确保 i + 2 不超过 1000
    for i in range(3, 999):
        if prime(i) and prime(i + 2):
            print("(%-3d, %3d)  " % (i, i + 2), end="")
            count += 1
            # 每 5 对孪生素数换一行
            if count % 5 == 0:
                print()

    # 结尾格式控制
    if count % 5 != 0:
        print()

    print("\n1000以内的孪生素数共有%d对" % count)


if __name__ == "__main__":
    main()