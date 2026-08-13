#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 可逆素数（查找所有 4 位可逆素数：自身是 4 位素数，且逆序数也是 4 位素数）

import math


def is_prime(n: int) -> bool:
    """判断一个整数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

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


def reverse_number(n: int) -> int:
    """计算一个正整数的逆序数（如 1234 -> 4321）。

    Args:
        n (int): 输入的正整数。

    Returns:
        int: 翻转后的正整数。
    """
    return int(str(n)[::-1])


def main() -> None:
    """主程序入口：穷举查找所有 4 位可逆素数并按每行 10 个格式化打印。"""
    count = 0
    print("【所有 4 位可逆素数列表】")

    # 四重循环穷举千位 a (1-9)、百位 b (0-9)、十位 c (0-9)、个位 d (1-9)
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(1, 10):
                    num = a * 1000 + b * 100 + c * 10 + d
                    rev_num = d * 1000 + c * 100 + b * 10 + a

                    # 判定原数及其逆序数是否均为素数
                    if is_prime(num) and is_prime(rev_num):
                        print(f"{num:<6d}", end="")
                        count += 1
                        # 每 10 个素数换一行
                        if count % 10 == 0:
                            print()

    # 结尾控制换行
    if count % 10 != 0:
        print()

    print(f"\n4位可逆素数共有{count}个")


if __name__ == "__main__":
    main()