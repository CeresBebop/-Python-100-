#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 按递增顺序依次列出所有分母小于等于40的最简真分数 (Irreducible Proper Fractions)

import math


def get_irreducible_proper_fractions(
    max_denominator: int = 40, sort_by_value: bool = True
) -> list[tuple[int, int]]:
    """获取所有分母小于等于 max_denominator 的最简真分数 (分子, 分母) 列表。

    真分数定义：0 < 分子 < 分母。
    最简分数定义：分子与分母互质，即 gcd(分子, 分母) == 1。

    Args:
        max_denominator (int): 最大分母上限，默认 40
        sort_by_value (bool): 是否按分数值大小（升序）严格排序。
                              True: 严格按数值从 0 到 1 递增排序（如 1/40 < 1/39 ...）；
                              False: 按原书逻辑按分母由小到大、分子由小到大分组排序。

    Returns:
        list[tuple[int, int]]: 包含 (分子, 分母) 元组的列表
    """
    fractions = []

    # 遍历分母 b (从 2 到 max_denominator)
    for b in range(2, max_denominator + 1):
        # 遍历分子 a (从 1 到 b - 1)
        for a in range(1, b):
            # 若分子分母互质，即为最简真分数
            if math.gcd(a, b) == 1:
                fractions.append((a, b))

    # 根据题目要求“按递增顺序”，对生成的真分数按实际数值 a/b 升序排序
    if sort_by_value:
        fractions.sort(key=lambda frac: frac[0] / frac[1])

    return fractions


def print_fraction_sequence(
    max_denominator: int = 40, items_per_line: int = 10, sort_by_value: bool = True
) -> None:
    """格式化打印指定分母上限内的最简真分数序列。

    Args:
        max_denominator (int): 分母上限，默认 40
        items_per_line (int): 每行显示的分数个数，默认 10
        sort_by_value (bool): 是否按数值大小递增排序，默认 True
    """
    sort_mode_str = "数值递增顺序" if sort_by_value else "分母分组顺序"
    print(f"=== 分母小于等于 {max_denominator} 的所有最简真分数（按 {sort_mode_str} 排列）===")

    fractions = get_irreducible_proper_fractions(
        max_denominator, sort_by_value=sort_by_value
    )

    print(f"共计 {len(fractions)} 个最简真分数：\n")

    for index, (a, b) in enumerate(fractions, start=1):
        # 使用 f-string 规范格式化对齐输出 (如: " 1/40")
        print(f"{a:2d}/{b:2d}", end="  ")

        # 每 items_per_line 个分数换行一次
        if index % items_per_line == 0:
            print()

    # 处理末行未满时的排版换行
    if len(fractions) % items_per_line != 0:
        print()


def main() -> None:
    """主程序入口。"""
    # 按照题目“按递增顺序”的要求，默认按分数值从 0 到 1 严格升序打印
    print_fraction_sequence(max_denominator=40, items_per_line=10, sort_by_value=True)


if __name__ == "__main__":
    main()