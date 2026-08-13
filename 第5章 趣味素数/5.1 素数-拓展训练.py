# Author: CeresBebop
# -*- coding: utf-8 -*-
"""拓展训练：寻找最小的 10 个连续合数（非素数）程序实现。"""

import math
from typing import List, Tuple


def is_composite(n: int) -> bool:
    """判断一个自然数是否为合数。

    合数定义：大于 1 的自然数中，除了 1 和它本身之外，还能被其他正整数整除的数。

    Args:
        n (int): 待检测的自然数。

    Returns:
        bool: 若为合数则返回 True，否则（如 <= 1 或素数）返回 False。
    """
    if n <= 3:
        return False
    # 排除 2 和 3 的倍数
    if n % 2 == 0 or n % 3 == 0:
        return True

    # 试除法检测因子
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False


def get_factor_proof(n: int) -> str:
    """获取合数的非平凡因数分解表达式，用于直观证明其为合数。

    Args:
        n (int): 目标合数。

    Returns:
        str: 如 '114 = 2 × 57' 的证明字符串。
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"{n} = {i} × {n // i}"
    return str(n)


def find_smallest_consecutive_composites(
    target_count: int = 10,
) -> Tuple[int, List[int]]:
    """高效查找连续 target_count 个合数的最小起始自然数及完整的数值序列。

    Args:
        target_count (int): 要求的连续合数数量，默认为 10。

    Returns:
        Tuple[int, List[int]]: (起始数值, 连续合数列表)。
    """
    current_num = 2
    consecutive_count = 0
    start_num = 0

    while True:
        if is_composite(current_num):
            if consecutive_count == 0:
                start_num = current_num
            consecutive_count += 1

            # 达成连续合数数量目标
            if consecutive_count == target_count:
                result_sequence = list(
                    range(start_num, start_num + target_count)
                )
                return start_num, result_sequence
        else:
            # 遇到素数或非合数，重置计数器
            consecutive_count = 0

        current_num += 1


def main() -> None:
    """主程序入口：执行搜索并格式化输出答案与验证证明。"""
    target_length = 10
    start_num, composite_list = find_smallest_consecutive_composites(
        target_length
    )

    print(
        f"【拓展训练解答】10 个最小的连续合数序列为: {start_num} ~ {start_num + target_length - 1}\n"
    )
    print(f"连续合数列表: {composite_list}\n")

    print("【每个数值的合数验证证明】")
    print("=" * 35)
    for idx, num in enumerate(composite_list, start=1):
        proof = get_factor_proof(num)
        print(f"第 {idx:2d} 个数: {num:<4d}  =>  ({proof})")
    print("=" * 35)


if __name__ == "__main__":
    main()