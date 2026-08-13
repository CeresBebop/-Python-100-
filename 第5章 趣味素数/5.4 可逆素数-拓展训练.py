# Author: CeresBebop
# -*- coding: utf-8 -*-
"""寻找并格式化输出指定范围内（默认 1000 以内）的所有孪生素数（Twin Primes）。

孪生素数定义：若自然数 a 为素数，且 a + 2 也是素数，则称素数对 (a, a + 2) 为孪生素数。
"""

import math
from typing import List, Tuple


def is_prime(n: int) -> bool:
    """判断一个整数是否为素数（质数）。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 试除法：遍历 3 到 sqrt(n) 之间的奇数因子
    max_factor = int(math.sqrt(n))
    for i in range(3, max_factor + 1, 2):
        if n % i == 0:
            return False
    return True


def find_twin_primes(limit: int = 1000) -> List[Tuple[int, int]]:
    """查找不超过上限 limit 的所有孪生素数对 (a, a + 2)。

    Args:
        limit (int): 数值上限，默认 1000。

    Returns:
        List[Tuple[int, int]]: 包含所有 (a, a + 2) 孪生素数对的列表。
    """
    twin_primes = []

    # 遍历区间 [2, limit - 2]，确保 a + 2 不超过上限 limit
    for a in range(2, limit - 1):
        if is_prime(a) and is_prime(a + 2):
            twin_primes.append((a, a + 2))

    return twin_primes


def main() -> None:
    """主程序入口：求解 1000 以内的孪生素数并以美化表格形式打印。"""
    limit = 1000
    twin_primes = find_twin_primes(limit)

    print(f"【{limit} 以内的所有孪生素数 (a, a + 2)】\n")

    count = 0
    for a, b in twin_primes:
        print(f"({a:3d}, {b:3d})  ", end="")
        count += 1
        # 每行美化打印 5 对孪生素数
        if count % 5 == 0:
            print()

    # 控制末尾换行
    if count % 5 != 0:
        print()

    print(f"\n在 {limit} 以内共找到 {count} 对孪生素数。")


if __name__ == "__main__":
    main()