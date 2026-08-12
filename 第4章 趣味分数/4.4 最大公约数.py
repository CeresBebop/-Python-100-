#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 求两个整数的最大公约数 (GCD) - 穷举法 (从大到小与从小到大两种思路)


def gcd_enum_descending(m: int, n: int) -> int:
    """按从大到小的顺序穷举求两个整数的最大公约数。

    算法原理（方法1）：
    从 min(|m|, |n|) 开始向下递减遍历到 1，遇到的第一个能同时整除 m 和 n 的数即为 GCD。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最大公约数
    """
    m_abs, n_abs = abs(m), abs(n)
    min_val = min(m_abs, n_abs)

    # 边界情况：若存在 0，直接返回另一个数的绝对值
    if min_val == 0:
        return max(m_abs, n_abs)

    # 从 min(|m|, |n|) 递减遍历到 1
    for i in range(min_val, 0, -1):
        if m_abs % i == 0 and n_abs % i == 0:
            return i

    return 1


def gcd_enum_ascending(m: int, n: int) -> int:
    """按从小到大的顺序穷举求两个整数的最大公约数。

    算法原理（方法2）：
    从 1 递增遍历到 min(|m|, |n|)，不断更新能够同时整除 m 和 n 的数 k，
    遍历结束后的 k 即为 GCD。

    Args:
        m (int): 第一个整数
        n (int): 第二个整数

    Returns:
        int: m 和 n 的最大公约数
    """
    m_abs, n_abs = abs(m), abs(n)
    min_val = min(m_abs, n_abs)

    if min_val == 0:
        return max(m_abs, n_abs)

    gcd_val = 1
    # 注意：必须遍历到 min_val 本身，即 range(1, min_val + 1)
    for i in range(1, min_val + 1):
        if m_abs % i == 0 and n_abs % i == 0:
            gcd_val = i

    return gcd_val


def main() -> None:
    """主程序入口，包含交互输入与零配置默认回退机制。"""
    print("=== 求两个整数的最大公约数 (GCD) ===")

    # 零配置容错：按下回车或输入为空时使用默认用例 m=24, n=36
    raw_input = input("请输入两个整数 m 和 n (空格分隔) [直接回车默认 m=24, n=36]: ").strip()

    if not raw_input:
        m, n = 24, 36
        print(f"未检测到输入，自动加载默认测试用例: m = {m}, n = {n}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != 2:
                raise ValueError("需要输入两个由空格分隔的整数")
            m, n = int(parts[0]), int(parts[1])
        except ValueError as err:
            print(f"输入格式解析失败 ({err})，自动加载默认测试用例: m = 24, n = 36")
            m, n = 24, 36

    # 方法 1：从大到小穷举
    res_desc = gcd_enum_descending(m, n)
    print(f"\n[方法1 - 从大到小穷举] {m} 和 {n} 的最大公约数是: {res_desc}")

    # 方法 2：从小到大穷举
    res_asc = gcd_enum_ascending(m, n)
    print(f"[方法2 - 从小到大穷举] {m} 和 {n} 的最大公约数是: {res_asc}")


if __name__ == "__main__":
    main()