#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 亲密数 (Amicable Numbers)

def sum_proper_divisors(num: int) -> int:
    """计算一个正整数的所有真因子（除自身以外的因数）之和。

    优化算法：采用时间复杂度为 O(sqrt(num)) 的快速因数分解法。
    通过成对提取因数，省去了原代码逐个数字遍历的巨大开销。

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

    亲密数定义：如果两个不同的正整数 a 和 b，a 的所有真因子之和等于 b，
    且 b 的所有真因子之和等于 a，则称 a 和 b 是一对亲密数。

    Args:
        limit (int): 检索范围的上限。
    """
    print(f"{limit}以内的全部亲密数为:")
    print(f"{'Num A':<8} -- {'Num B':<8}")
    print("-" * 22)
    
    for a in range(1, limit):
        # 计算 a 的真因子之和 b
        b = sum_proper_divisors(a)
        
        # 性能关键优化点：
        # 1. 亲密数对要求 a != b（排除完数，如 6 = 1+2+3）；
        # 2. 为了避免重复打印（如 220--284 和 284--220），只在 a < b 时才进行双向验证。
        # 若 b <= a，则无需对 b 进行昂贵的二次因子求和，直接跳过。
        if b <= a:
            continue
            
        # 计算 b 的真因子之和 n
        n = sum_proper_divisors(b)
        
        # 如果 n 回到了 a，说明互为亲密数
        if n == a:
            print(f"{a:<8d} -- {b:<8d}")


if __name__ == '__main__':
    find_amicable_pairs(3000)