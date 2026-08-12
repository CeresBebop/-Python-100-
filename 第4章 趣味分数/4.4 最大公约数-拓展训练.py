#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 拓展训练：求满足“被 2~10 除余数均为 n-1”的最小正整数（最小公倍数 LCM 算法）

import math


def find_smallest_number_by_lcm(start_n: int = 2, end_n: int = 10) -> int:
    """利用最小公倍数 (LCM) 数学原理直接求解目标正整数，完全规避暴力枚举与逐个试除。

    数学推导证明：
    设所求正整数为 x，已知对任意 n ∈ [2, 10]，均满足：
        x % n = n - 1
    即：
        x + 1 ≡ 0 (mod n)
    说明 (x + 1) 能够同时被 2, 3, 4, 5, 6, 7, 8, 9, 10 整除。
    要使 x 为最小正整数，(x + 1) 必须是 2~10 所有整数的【最小公倍数 (LCM)】。
    故：x = LCM(2, 3, 4, 5, 6, 7, 8, 9, 10) - 1。

    Args:
        start_n (int): 除数范围起始值，默认为 2
        end_n (int): 除数范围结束值，默认为 10

    Returns:
        int: 满足条件的最小正整数 x
    """
    # 利用 Python 标准库计算 2~10 所有整数的最小公倍数 LCM
    lcm_val = math.lcm(*range(start_n, end_n + 1))

    # 目标正整数即为 LCM - 1
    target_number = lcm_val - 1
    return target_number


def verify_solution(x: int, start_n: int = 2, end_n: int = 10) -> bool:
    """校验求出的正整数 x 是否严格满足任意 n in [start_n, end_n] 下余数均等于 n - 1。

    Args:
        x (int): 待验证的正整数
        start_n (int): 起始除数，默认 2
        end_n (int): 结束除数，默认 10

    Returns:
        bool: 是否全部符合要求
    """
    for n in range(start_n, end_n + 1):
        if x % n != n - 1:
            return False
    return True


def main() -> None:
    """主程序入口。"""
    start_n, end_n = 2, 10

    print(f"=== 求被任意 {start_n}~{end_n} 除余数均为 n-1 的最小正整数 ===")

    # 计算目标值
    result = find_smallest_number_by_lcm(start_n, end_n)
    print(f"\n[数学求解结果] 最小正整数 x = {result}")

    # 验证答案正确性
    is_valid = verify_solution(result, start_n, end_n)
    print(f"[验证结论] {'验证通过 (True)' if is_valid else '验证失败 (False)'}")

    # 打印逐项余数校验表
    print("\n详细校验列表：")
    for n in range(start_n, end_n + 1):
        remainder = result % n
        print(f"  {result} % {n:2d} = {remainder:2d}  (期望余数 n-1 = {n-1})")


if __name__ == "__main__":
    main()