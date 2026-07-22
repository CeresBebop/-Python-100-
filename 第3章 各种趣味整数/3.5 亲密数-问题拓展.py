#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 亲密数 (重构与致命 Bug 修复版)

def sum_proper_divisors(num: int) -> int:
    """计算一个正整数的所有真因子之和。

    采用时间复杂度为 O(sqrt(num)) 的快速因数分解算法，
    极大地提升了因数求和性能，避免了原代码的性能瓶颈。

    Args:
        num (int): 输入的正整数。

    Returns:
        int: 该数的所有真因子之和。
    """
    if num <= 1:
        return 0
    total = 1  # 1 必定是任意大于 1 的正整数的真因子
    
    # 仅需遍历到 num 的平方根
    limit = int(num ** 0.5)
    for i in range(2, limit + 1):
        if num % i == 0:
            total += i
            other = num // i
            if other != i:  # 避免对完全平方数重复累加相同的平方根
                total += other
    return total


def find_amicable_pairs(limit: int = 3000) -> None:
    """寻找并优雅地打印指定上限内的所有亲密数对。

    此函数已彻底修复原代码中由于变量作用域不当引发的致命累加 Bug。

    Args:
        limit (int): 检索范围的上限。
    """
    print(f"{limit}以内的全部亲密数为:")
    print(f"{'Num A':<8} -- {'Num B':<8}")
    print("-" * 22)
    
    # 修正：原书范围 range(3000) 包含了 0，而亲密数是针对正整数定义的，应从 1 开始
    for a in range(1, limit):
        # 修正：【致命 Bug 修复】变量 b 和 n 必须在每次循环开始时重置为 0！
        # 原书将它们定义在 for 循环外部，导致它们在整个循环中充当了“全局累加器”，
        # 从而不断累加所有数字的因子，产生彻底错误的运行结果。
        b = sum_proper_divisors(a)
        
        # 性能优化：只在 a < b 时才进行双向验证，若 b <= a 则直接跳过
        if b <= a:
            continue
            
        n = sum_proper_divisors(b)
        
        # 如果 n 回到了 a，说明互为亲密数
        if n == a:
            print(f"{a:<8d} -- {b:<8d}")


if __name__ == '__main__':
    find_amicable_pairs(3000)