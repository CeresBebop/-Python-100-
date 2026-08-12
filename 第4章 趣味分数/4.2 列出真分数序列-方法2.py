#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 列出真分数序列——利用穷举试除法判断分子与分母是否互质 (Method 2)


def is_coprime_by_trial_division(num1: int, num2: int) -> bool:
    """利用穷举试除法判断两个正整数是否互质（即是否存在大于 1 的公约数）。

    算法原理（方法2 - 试除法）：
    遍历公因子 j 从 2 到 min(num1, num2)。若存在某个 j 能同时整除分子和分母，
    说明该分数非最简分数（不互质）；若循环结束未发现公因子，则说明两者互质。

    Args:
        num1 (int): 第一个正整数（分母）
        num2 (int): 第二个正整数（分子）

    Returns:
        bool: True 表示互质（最简真分数），False 表示存在公约数
    """
    min_val = min(num1, num2)

    # 穷举试除 2 ~ min(num1, num2) 范围内的整数
    for j in range(2, min_val + 1):
        if num1 % j == 0 and num2 % j == 0:
            return False  # 找到公约数，直接返回不互质

    return True  # 遍历完成未找到公约数，两者互质


def get_irreducible_fractions_trial(denominator: int = 40) -> list[int]:
    """获取指定分母下所有分子小于分母的最简真分数的分子列表。

    Args:
        denominator (int): 分母（正整数）

    Returns:
        list[int]: 符合条件的最简真分数的分子列表
    """
    irreducible_numerators = []

    # 穷举分子 1 到 denominator - 1
    for numerator in range(1, denominator):
        # 判定分子和分母是否互质
        if is_coprime_by_trial_division(denominator, numerator):
            irreducible_numerators.append(numerator)

    return irreducible_numerators


def print_irreducible_fractions(
    denominator: int = 40, items_per_line: int = 8
) -> None:
    """格式化打印最简真分数序列，按每行固定数量输出。

    Args:
        denominator (int): 分母，默认为 40
        items_per_line (int): 每行显示的分数个数，默认为 8
    """
    print(f"分母为{denominator}，分子小于{denominator}的最简分数有: ")

    numerators = get_irreducible_fractions_trial(denominator)

    for index, numerator in enumerate(numerators, start=1):
        # 使用 f-string 对齐格式化输出
        print(f"{numerator:2d}/{denominator}", end="  ")

        # 每 8 个分数换行一次
        if index % items_per_line == 0:
            print()

    # 处理末行未满时的排版兜底换行
    if len(numerators) % items_per_line != 0:
        print()


def main() -> None:
    """主程序入口。"""
    print_irreducible_fractions(denominator=40, items_per_line=8)


if __name__ == "__main__":
    main()