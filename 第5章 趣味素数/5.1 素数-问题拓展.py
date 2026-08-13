# Author: CeresBebop
# -*- coding: utf-8 -*-
"""素数（质数）判定的两种算法实现与对比。

包含：
1. 基础遍历试除法 (循环范围：2 ~ m-1)
2. 平方根优化试除法 (循环范围：2 ~ sqrt(m))
"""

import math


def is_prime_basic(m: int) -> bool:
    """方法一：基础试除法判断 m 是否为素数（遍历范围：2 ~ m-1）。

    Args:
        m (int): 待判断的整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    # 1 及小于 1 的整数均不是素数
    if m < 2:
        return False

    # 循环边界必须为 i < m（原代码中 i <= m 会导致 m % m == 0 始终成立而将所有数误判为非素数）
    i = 2
    while i < m:
        if m % i == 0:
            return False
        i += 1
    return True


def is_prime_optimized(m: int) -> bool:
    """方法二：平方根优化试除法判断 m 是否为素数（遍历范围：2 ~ sqrt(m)）。

    Args:
        m (int): 待判断的整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    # 1 及小于 1 的整数均不是素数
    if m < 2:
        return False

    # 计算 sqrt(m) 的整数上限
    k = int(math.sqrt(m))

    # 遍历范围为 [2, k]，无需多加 1
    for i in range(2, k + 1):
        if m % i == 0:
            return False
    return True


def check_and_print_prime(m: int) -> None:
    """打印指定整数在两种判定方法下的判定结果。

    Args:
        m (int): 待判定的目标整数。
    """
    print(f"\n===== 测试整数: m = {m} =====")

    # 1. 基础遍历法测试
    result_basic = "是素数！" if is_prime_basic(m) else "不是素数！"
    print(f"[基础法 (2~m-1)]      : {m} {result_basic}")

    # 2. 平方根优化法测试
    result_opt = "是素数！" if is_prime_optimized(m) else "不是素数！"
    print(f"[优化法 (2~sqrt(m))]: {m} {result_opt}")


def main() -> None:
    """主函数：运行预设测试用例并提供交互式输入接口。"""
    # 自动运行预设测试数据（涵盖负数、0、1、偶数、合数、素数）
    test_cases = [1, 2, 3, 4, 9, 17, 25, 29]
    print("【自动运行预设测试用例】")
    for num in test_cases:
        check_and_print_prime(num)

    # 交互式测试
    print("\n" + "=" * 40)
    try:
        user_input = input("请输入要判定的整数 m (直接回车跳过): ").strip()
        if user_input:
            m = int(user_input)
            check_and_print_prime(m)
    except ValueError:
        print("输入解析失败：请输入有效的整数！")


if __name__ == "__main__":
    main()