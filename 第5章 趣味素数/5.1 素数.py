#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 查找并输出指定闭区间内的所有素数（质数）

import math


def is_prime(n: int) -> bool:
    """判断一个整数是否为素数（质数）。

    Args:
        n (int): 待判断的正整数。

    Returns:
        bool: 若 n 为素数则返回 True，否则返回 False。
    """
    # 1 及小于 1 的整数均不是素数
    if n < 2:
        return False
    # 2 是最小的素数，也是唯一的偶数素数
    if n == 2:
        return True
    # 排除大于 2 的偶数
    if n % 2 == 0:
        return False

    # 只需要检查到 sqrt(n) 的奇数因子即可
    max_factor = int(math.sqrt(n))
    for i in range(3, max_factor + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes_in_range(start: int, end: int) -> int:
    """计算并格式化输出区间 [start, end] 内的所有素数。

    Args:
        start (int): 区间起始整数。
        end (int): 区间结束整数。

    Returns:
        int: 该区间内统计到的素数总个数。
    """
    count = 0
    print(f"\n{start} 和 {end} 之间的素数有:")

    # 对 start~end 闭区间内的每个数进行迭代检查
    for num in range(start, end + 1):
        if is_prime(num):
            print(f"{num:<4d}", end="")
            count += 1
            # 每 15 个素数换行输出
            if count % 15 == 0:
                print()

    print(f"\n\n{start} 到 {end} 之间共有: {count} 个素数")
    return count


def main() -> None:
    """主程序入口：获取用户输入的范围区间并执行素数查找逻辑。"""
    print("请输入一个整数范围(start-end): ")

    while True:
        try:
            start = int(input("start = "))
            end = int(input("end = "))
            # 校验输入的合法性：start 必须大于 0 且小于 end
            if start > 0 and start < end:
                break
            print("输入的参数有误（须满足 start > 0 且 start < end），请重新输入: ")
        except ValueError:
            print("输入格式错误，请输入有效的整型数值！请重新输入: ")

    # 执行素数检索与结果打印
    print_primes_in_range(start, end)


if __name__ == "__main__":
    main()