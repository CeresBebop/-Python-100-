# Author: CeresBebop
# -*- coding: utf-8 -*-
"""基于奇偶性拆分与奇数步长（+2）优化的素数判定算法实现。

原理说明：
1. 2 是唯一的偶素数，所有大于 2 的偶数必然是合数。
2. 奇数的因数也必然是奇数，因此只需遍历 3 ~ sqrt(n) 之间的奇数（步长为 2），能减少一半的试除计算量。
"""

import math


def is_prime(n: int) -> bool:
    """判断一个整数是否为素数（包含边界拦截、奇偶拆分与步长 2 优化）。

    Args:
        n (int): 待检测的目标整数。

    Returns:
        bool: 若为素数返回 True，否则（如 <= 1 或合数）返回 False。
    """
    # 修复原代码 Bug 1：1 及小于 1 的整数均不是素数（原代码对 1 会误判为素数）
    # 修复原代码 Bug 2：防止负数传入 math.sqrt(n) 时触发 ValueError: math domain error
    if n < 2:
        return False

    # 2 是唯一的偶素数
    if n == 2:
        return True

    # 排除所有大于 2 的偶数
    if n % 2 == 0:
        return False

    # 奇数的因子只能是奇数，从 3 开始，步长自增 2
    max_factor = int(math.sqrt(n))
    i = 3
    while i <= max_factor:
        if n % i == 0:
            return False
        i += 2

    return True


def fun(n: int) -> int:
    """原代码接口的兼容实现（返回 1 表示素数，0 表示非素数）。

    Args:
        n (int): 待检测的整数。

    Returns:
        int: 是素数返回 1，非素数返回 0。
    """
    return 1 if is_prime(n) else 0


def main() -> None:
    """主程序入口：自动运行边缘与代表性测试用例，并提供交互式输入测试。"""
    # 测试集涵盖：负数、0、1、2（偶素数）、偶合数、奇素数、奇合数
    test_cases = [-3, 0, 1, 2, 3, 4, 9, 15, 17, 25, 97]

    print("【奇偶性与步长 2 优化试除法 - 自动用例测试】")
    print("-" * 45)
    print(f"{'测试数值 (n)':<12} | {'fun(n) 返回值':<12} | {'判定结论':<10}")
    print("-" * 45)

    for num in test_cases:
        res = fun(num)
        status = "素数" if res == 1 else "非素数"
        print(f"{num:<14d} | {res:<14d} | {status}")

    print("-" * 45)

    # 交互输入界面
    print("\n【交互测试】请输入要判定的整数（按 Ctrl+C 或直接回车退出）:")
    while True:
        try:
            user_input = input("n = ").strip()
            if not user_input:
                print("程序已安全退出。")
                break
            n = int(user_input)
            res = fun(n)
            print(
                f"数值 {n} 的判断结果: {res} -> ({'素数' if res == 1 else '非素数'})\n"
            )
        except ValueError:
            print("输入错误：请输入有效的整数！\n")
        except (KeyboardInterrupt, EOFError):
            print("\n程序已终止。")
            break


if __name__ == "__main__":
    main()