#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 最大公约数——辗转相除法 (Euclidean Algorithm for GCD)


def gcd_euclidean(m: int, n: int) -> int:
    """利用辗转相除法（欧几里得算法）计算两个整数的最大公约数。

    算法原理：
    gcd(m, n) = gcd(n, m % n)。反复用除数除以余数，直到余数为 0，
    此时非零的除数即为最大公约数。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最大公约数 (GCD)
    """
    # 取绝对值以兼容负数输入
    a, b = abs(m), abs(n)

    # 简洁的 Pythonic 辗转相除迭代：无需显式交换 a 和 b，a % b 会自动调整顺序
    while b != 0:
        a, b = b, a % b

    return a


def main() -> None:
    """主程序入口，支持交互输入与零配置默认回退逻辑。"""
    print("=== 最大公约数计算程序（辗转相除法）===")

    # 零配置容错：空输入或直接按下回车时，自动使用默认测试用例 m=48, n=18
    raw_input = input("请输入两个整数 m 和 n (空格分隔) [直接回车默认 m=48, n=18]: ").strip()

    if not raw_input:
        m, n = 48, 18
        print(f"未检测到输入，自动加载默认测试用例: m = {m}, n = {n}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != 2:
                raise ValueError("必须输入两个由空格分隔的整数")
            m, n = int(parts[0]), int(parts[1])
        except ValueError as err:
            print(f"输入格式解析失败 ({err})，自动加载默认测试用例: m = 48, n = 18")
            m, n = 48, 18

    # 调用辗转相除法计算 GCD
    result = gcd_euclidean(m, n)
    print(f"{m} 和 {n} 的最大公约数是: {result}")


if __name__ == "__main__":
    main()