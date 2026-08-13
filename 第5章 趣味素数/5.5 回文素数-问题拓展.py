# Author: CeresBebop
# -*- coding: utf-8 -*-
"""判断/查找回文素数的多种替代方法实现与性能对比。

问题拓展探讨：除了“遍历自然数 + 字符串转置 + 素数检测”外，有哪些更高效或不同维度的判断/生成方法？

方法一：纯数学按位翻转法（不使用字符串转换，仅靠算术运算提取与构造逆序数）。
方法二：回文数直接生成法 + 数学定理剪枝（直接镜像构造回文数再判断素性；利用“除 11 外所有偶数位的回文数必为 11 的倍数”这一定理跳过偶数位数）。
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """试除法判断一个整数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_factor = int(math.sqrt(n))
    for i in range(3, max_factor + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome_math(n: int) -> bool:
    """【替代方法一】纯数学算术翻转法判断回文数（不依赖字符串）。

    算法原理：通过取模（% 10）提取最低位，并通过整除（// 10）和乘 10 累加构造逆序数。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 若为回文数返回 True，否则返回 False。
    """
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + (n % 10)
        n //= 10

    return original == reversed_num


def generate_palindromic_primes(limit: int = 1000) -> List[int]:
    """【替代方法二】回文数构造生成法（利用数学定理进行高效剪枝）。

    核心数学剪枝定理：
    1. 除 11 外，所有偶数位数的回文数（如 1221, 123321）都能被 11 整除，因此绝对不可能是素数！
    2. 多位回文素数的首尾数字只能是 1, 3, 7, 9（首尾若为偶数或 5 则必定是合数）。

    Args:
        limit (int): 查找上限，默认 1000。

    Returns:
        List[int]: 范围内所有的回文素数列表。
    """
    results = []

    # 1. 基础处理单位数素数 (2, 3, 5, 7) 和唯一的偶数位回文素数 11
    base_primes = [2, 3, 5, 7, 11]
    for p in base_primes:
        if p <= limit:
            results.append(p)

    # 2. 仅构造 3 位数回文数：格式为 'a b a' (a 取 1, 3, 7, 9; b 取 0~9)
    # 直接绕过了所有的偶数位数（如 4 位数），极大减少无效检测
    for a in [1, 3, 7, 9]:
        for b in range(10):
            num = a * 100 + b * 10 + a
            if num > limit:
                break
            if is_prime(num):
                results.append(num)

    results.sort()
    return results


def main() -> None:
    """主程序入口：演示并对比两种替代方法的运行结果。"""
    limit = 1000

    print("==========================================")
    print(f"【方法一：纯数学按位翻转法（检测 2 ~ {limit}）】")
    print("==========================================")
    math_results = []
    for num in range(2, limit + 1):
        if is_palindrome_math(num) and is_prime(num):
            math_results.append(num)

    for idx, p in enumerate(math_results, start=1):
        print(f"{p:<6d}", end="")
        if idx % 10 == 0:
            print()
    if len(math_results) % 10 != 0:
        print()
    print(f"总计找到: {len(math_results)} 个回文素数\n")

    print("==========================================")
    print(f"【方法二：回文数构造生成法（11 整除定理剪枝）】")
    print("==========================================")
    gen_results = generate_palindromic_primes(limit)

    for idx, p in enumerate(gen_results, start=1):
        print(f"{p:<6d}", end="")
        if idx % 10 == 0:
            print()
    if len(gen_results) % 10 != 0:
        print()
    print(f"总计找到: {len(gen_results)} 个回文素数")


if __name__ == "__main__":
    main()