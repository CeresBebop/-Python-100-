#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 求两个整数的最小公倍数 (LCM) - 包含公式法 (利用 GCD) 与 递增穷举法


def gcd_euclidean(m: int, n: int) -> int:
    """利用辗转相除法（欧几里得算法）计算最大公约数。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最大公约数 (GCD)
    """
    a, b = abs(m), abs(n)
    while b != 0:
        a, b = b, a % b
    return a


def lcm_by_gcd(m: int, n: int) -> int:
    """利用公式 LCM(m, n) = |m * n| / GCD(m, n) 高效计算最小公倍数。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最小公倍数 (LCM)
    """
    if m == 0 or n == 0:
        return 0

    gcd_val = gcd_euclidean(m, n)
    return abs(m * n) // gcd_val


def lcm_by_enumeration(m: int, n: int) -> int:
    """利用递增穷举法寻找最小公倍数。

    从 max(|m|, |n|) 开始递增测试，遇到的第一个能同时被 m 和 n 整除的数即为 LCM。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最小公倍数 (LCM)
    """
    if m == 0 or n == 0:
        return 0

    m_abs, n_abs = abs(m), abs(n)
    i = max(m_abs, n_abs)

    while True:
        if i % m_abs == 0 and i % n_abs == 0:
            return i
        i += 1


def main() -> None:
    """主程序入口，支持交互输入与零配置默认回退逻辑。"""
    print("=== 求两个整数的最小公倍数 (LCM) ===")

    # 零配置容错：空输入或直接按下回车时，自动加载默认测试用例 m = 12, n = 18
    raw_input = input("请输入两个整数 m 和 n (空格分隔) [直接回车默认 m=12, n=18]: ").strip()

    if not raw_input:
        m, n = 12, 18
        print(f"未检测到输入，自动加载默认测试用例: m = {m}, n = {n}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != 2:
                raise ValueError("必须输入两个由空格分隔的整数")
            m, n = int(parts[0]), int(parts[1])
        except ValueError as err:
            print(f"输入格式解析失败 ({err})，自动加载默认测试用例: m = 12, n = 18")
            m, n = 12, 18

    # 方法 1：利用 GCD 的公式法 (O(log(min(m,n))) 时间复杂度)
    res_gcd = lcm_by_gcd(m, n)
    print(f"\n[方法1 - 公式法(利用GCD)] {m} 和 {n} 的最小公倍数是: {res_gcd}")

    # 方法 2：递增穷举搜索法
    res_enum = lcm_by_enumeration(m, n)
    print(f"[方法2 - 递增穷举搜索法] {m} 和 {n} 的最小公倍数是: {res_enum}")


if __name__ == "__main__":
    main()