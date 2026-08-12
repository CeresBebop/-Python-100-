#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 分数比较 - 利用通分法（求公分母 LCM）比较两个分数的大小

import math
from fractions import Fraction


def get_lcm(a: int, b: int) -> int:
    """计算两个整数的最小公倍数 (LCM)。

    Args:
        a (int): 第一个整数（分母 1）
        b (int): 第二个整数（分母 2）

    Returns:
        int: a 和 b 的最小公倍数

    Raises:
        ValueError: 当分母为 0 时抛出
    """
    if a == 0 or b == 0:
        raise ValueError("分数的分母不能为 0")
    return abs(a * b) // math.gcd(a, b)


def compare_fractions(i: int, j: int, k: int, l: int) -> str:
    """比较两个分数 i/j 和 k/l 的大小（采用通分法）。

    通分比较原理：
    1. 求出两分数分母 j 和 l 的最小公倍数 L 作为公分母。
    2. 将两分数通分：分子分别为 m = (L // j) * i，n = (L // l) * k。
    3. 比较通分后的分子 m 和 n 的大小。

    Args:
        i (int): 第一个分数的分子
        j (int): 第一个分数的分母
        k (int): 第二个分数的分子
        l (int): 第二个分数的分母

    Returns:
        str: 比较运算符字符串 ('>', '=', 或 '<')
    """
    if j == 0 or l == 0:
        raise ValueError("分数的分母不能为 0")

    # 1. 计算公分母 (最小公倍数 LCM)
    common_denom = get_lcm(j, l)

    # 2. 通分后求各自新的分子
    m = (common_denom // j) * i
    n = (common_denom // l) * k

    # 3. 比较分子大小
    if m > n:
        return ">"
    elif m < n:
        return "<"
    else:
        return "="


def parse_fraction_input(input_str: str) -> tuple[int, int]:
    """解析分数字符串，同时兼容 '4/5' 与 '4 5' 两种常见的输入格式。

    Args:
        input_str (str): 用户输入的字符串

    Returns:
        tuple[int, int]: (分子, 分母) 元组

    Raises:
        ValueError: 当格式不匹配或分母为 0 时抛出
    """
    s = input_str.strip()
    if "/" in s:
        parts = s.split("/")
    else:
        parts = s.split()

    if len(parts) != 2:
        raise ValueError("请输入格式如 '4/5' 或 '4 5' 的分子和分母")

    numerator, denominator = int(parts[0]), int(parts[1])
    if denominator == 0:
        raise ValueError("分母不能为 0")

    return numerator, denominator


def main() -> None:
    """主程序入口，支持交互输入与零配置默认回退逻辑。"""
    print("=== 分数大小比较程序 ===")

    # 零配置容错：直接按回车默认使用用例 4/5 和 3/4
    input1 = input("请输入第一个分数 (如 '4/5' 或 '4 5') [直接回车默认 4/5]: ").strip()
    input2 = input("请输入第二个分数 (如 '3/4' 或 '3 4') [直接回车默认 3/4]: ").strip()

    # 解析第一个分数
    if not input1:
        i, j = 4, 5
    else:
        try:
            i, j = parse_fraction_input(input1)
        except ValueError as err:
            print(f"第一个分数输入格式无效 ({err})，自动加载默认值 4/5")
            i, j = 4, 5

    # 解析第二个分数
    if not input2:
        k, l = 3, 4
    else:
        try:
            k, l = parse_fraction_input(input2)
        except ValueError as err:
            print(f"第二个分数输入格式无效 ({err})，自动加载默认值 3/4")
            k, l = 3, 4

    print(f"\n第一个分数: {i}/{j}")
    print(f"第二个分数: {k}/{l}")

    # 执行通分比较
    relation = compare_fractions(i, j, k, l)
    print(f"比较结果: {i}/{j} {relation} {k}/{l}")

    # 标准库 Fraction 模块二次校验
    f1, f2 = Fraction(i, j), Fraction(k, l)
    print(f"(Standard Fraction 校验: {f1} 与 {f2} 的差值为 {f1 - f2})")


if __name__ == "__main__":
    main()