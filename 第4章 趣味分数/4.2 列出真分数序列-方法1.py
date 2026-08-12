#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 列出真分数序列——利用辗转相除法 (List Irreducible Proper Fractions)


def gcd_euclidean(a: int, b: int) -> int:
    """利用辗转相除法（欧几里得算法）计算两个正整数的最大公约数。

    Args:
        a (int): 第一个正整数（通常为分母）
        b (int): 第二个正整数（通常为分子）

    Returns:
        int: a 和 b 的最大公约数 (GCD)
    """
    while b != 0:
        a, b = b, a % b
    return a


def get_irreducible_fractions(denominator: int) -> list[int]:
    """计算并获取指定分母下所有分子小于分母的最简真分数（互质分子）。

    Args:
        denominator (int): 分母（正整数）

    Returns:
        list[int]: 符合条件的最简真分数的分子列表
    """
    irreducible_numerators = []
    # 穷举分子：从 1 到 denominator - 1
    for numerator in range(1, denominator):
        # 若分子与分母的最大公约数为 1，说明两者互质，即该分数为最简分数
        if gcd_euclidean(denominator, numerator) == 1:
            irreducible_numerators.append(numerator)
    return irreducible_numerators


def print_fractions(denominator: int = 40, items_per_line: int = 8) -> None:
    """格式化打印最简真分数序列，支持自定义分母与每行显示数量。

    Args:
        denominator (int): 分母，默认 40
        items_per_line (int): 每行显示的分数个数，默认 8
    """
    print(f"分母为{denominator}，分子小于{denominator}的最简分数有: ")

    numerators = get_irreducible_fractions(denominator)

    for count, numerator in enumerate(numerators, start=1):
        # 使用 f-string 格式化输出，保持宽度对齐
        print(f"{numerator:2d}/{denominator}", end="  ")

        # 每达到指定个数则进行换行
        if count % items_per_line == 0:
            print()

    # 如果最后一行未刚好满行，补齐末尾换行
    if len(numerators) % items_per_line != 0:
        print()


def main() -> None:
    """主程序入口。"""
    print_fractions(denominator=40, items_per_line=8)


if __name__ == "__main__":
    main()