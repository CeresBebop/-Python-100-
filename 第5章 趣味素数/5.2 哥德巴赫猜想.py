#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 验证哥德巴赫猜想（任何大于 2 的偶数都可以表示为两个素数之和）

import math


def is_prime(n: int) -> bool:
    """判断一个整数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

    Returns:
        bool: 若为素数返回 True，否则返回 False。
    """
    # 1 及小于 1 的整数均不是素数
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 只需要检查到 sqrt(n) 范围内的奇数
    max_factor = int(math.sqrt(n))
    i = 3
    while i <= max_factor:
        if n % i == 0:
            return False
        i += 2
    return True


def verify_goldbach(n: int) -> bool:
    """验证并打印大于 2 的偶数 n 的哥德巴赫猜想拆分方案。

    Args:
        n (int): 需要验证的目标偶数 (要求 n > 2)。

    Returns:
        bool: 若找到素数对并成功验证打印返回 True，否则返回 False。
    """
    # 哥德巴赫猜想仅适用于大于 2 的偶数
    if n <= 2 or n % 2 != 0:
        print(f"输入提示：{n} 不是大于 2 的偶数，不符合哥德巴赫猜想验证条件！")
        return False

    # 优先检查唯一的偶素数 2
    if is_prime(2) and is_prime(n - 2):
        print(f"{n} = 2 + {n - 2}")
        return True

    # 之后只需在大于 2 的奇数素数中递增查找
    i = 3
    while i <= n // 2:
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n - i}")
            return True
        i += 2

    return False


def main() -> None:
    """主程序入口：先自动运行预设示例，再提供交互式输入验证。"""
    # 运行运行结果示例数据 (4, 6, 8, 10, 12)
    print("【自动运行预设示例验证（4, 6, 8, 10, 12）】")
    test_cases = [4, 6, 8, 10, 12]
    for num in test_cases:
        verify_goldbach(num)

    print("\n" + "=" * 40)
    print("【交互模式】请输入大于 2 的偶数进行验证（直接回车退出）:")

    while True:
        try:
            user_input = input("n = ").strip()
            if not user_input:
                print("程序已安全退出。")
                break
            n = int(user_input)
            verify_goldbach(n)
        except ValueError:
            print("输入格式错误：请输入有效的整数！")
        except (KeyboardInterrupt, EOFError):
            print("\n程序终止。")
            break


if __name__ == "__main__":
    main()