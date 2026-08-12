#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 将真分数分解为埃及分数 (Egyptian Fraction Decomposition)

import math


def decompose_to_egyptian_fractions(a: int, b: int) -> list[int]:
    """将真分数 a/b 分解为若干互不相同的埃及分数（单位分数 1/c）的分母列表。

    算法原理：
    采用贪心算法（Greedy Algorithm）逐步减去不大于当前分数的最大单位分数。
    同时包含针对 3/b (b为偶数) 特殊情况的速算优化。

    Args:
        a (int): 分子 (要求 0 < a < b)
        b (int): 分母

    Returns:
        list[int]: 分解后各个埃及分数的分母列表，例如 [2, 5, 55, 110] 表示 1/2 + 1/5 + 1/55 + 1/110

    Raises:
        ValueError: 当传入的分数不是有效的真分数时抛出
    """
    if a <= 0 or b <= 0 or a >= b:
        raise ValueError("请输入有效的真分数（分子大于0且小于分母）")

    # 初始约分
    common_gcd = math.gcd(a, b)
    a //= common_gcd
    b //= common_gcd

    denominators = []

    while True:
        # 每轮循环前先进行最大公约数约分，防止数值暴涨
        gcd_val = math.gcd(a, b)
        a //= gcd_val
        b //= gcd_val

        # 情况 1：分子为 1，直接得到结果并退出
        if a == 1:
            denominators.append(b)
            break

        # 特殊情况优化：当分子为 3 且分母为偶数时，3/b 可直接拆分为 1/(b//2) + 1/b
        if a == 3 and b % 2 == 0:
            denominators.append(b // 2)
            denominators.append(b)
            break

        # 情况 2：分子不能整除分母，计算大于 a/b 的最小倒数整数 c = ceil(b / a)
        if b % a != 0:
            c = b // a + 1
        else:
            # 情况 3：分子能整除分母
            c = b // a
            denominators.append(c)
            break

        denominators.append(c)

        # 更新剩余分数：a/b - 1/c = (a * c - b) / (b * c)
        a = a * c - b
        b = b * c

    return denominators


def main() -> None:
    """主程序入口，支持命令行交互并带有零配置回退机制。"""
    print("=== 埃及分数分解程序 ===")

    # 提示用户输入，在无输入/直接回车时使用默认用例 8/11，确保无需配置即可直接一键运行
    raw_input = input(
        "请输入真分数的分子和分母（空格分隔，例如 '8 11'，直接回车运行默认用例）: "
    ).strip()

    if not raw_input:
        a, b = 8, 11
        print(f"未检测到输入，自动加载默认测试用例: {a}/{b}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != 2:
                raise ValueError("必须输入两个由空格分隔的整数")
            a, b = int(parts[0]), int(parts[1])
        except ValueError as err:
            print(f"输入格式解析失败 ({err})，将自动回退使用默认测试用例 8/11。")
            a, b = 8, 11

    print(f"输入的分数为: {a}/{b}")

    try:
        denominators = decompose_to_egyptian_fractions(a, b)
        result_expression = " + ".join([f"1/{d}" for d in denominators])
        print(f"埃及分数表示为: {result_expression}")
    except ValueError as e:
        print(f"计算错误: {e}")


if __name__ == "__main__":
    main()