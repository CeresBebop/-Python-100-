#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 多项式之和 - 递推优化算法 (Method 2: O(n) Factorial Reciprocal Sum)


def sum_factorial_reciprocals_fast(n: int) -> float:
    """计算多项式之和 S = 1/1! + 1/2! + 1/3! + ... + 1/n!。

    算法原理（方法2 - 递推法）：
    利用前后项递推关系：t_i = 1/i! = (1/(i-1)!) * (1/i) = t_{i-1} / i。
    相比于每次重新计算 i 的阶乘，该方法无需嵌套循环，将时间复杂度从 O(n^2) 降至 O(n)。

    Args:
        n (int): 项数上限，必须是大于等于 1 的正整数

    Returns:
        float: 多项式累加和 S

    Raises:
        ValueError: 当输入的 n 小于 1 时抛出
    """
    if n < 1:
        raise ValueError("输入参数 n 必须是大于等于 1 的正整数")

    s = 0.0
    t = 1.0  # 递推项中间变量

    # 单重循环累加，时间复杂度仅为 O(n)
    for i in range(1, n + 1):
        t = t / i  # 递推求解当前项 1/i!
        s += t  # 累加至总和

    return s


def main() -> None:
    """主程序入口，包含交互输入与零配置默认回退机制。"""
    print("=== 多项式之和计算程序（递推优化版: S = 1/1! + 1/2! + ... + 1/n!）===")

    # 零配置容错处理：若无输入或按回车，自动默认运行 n = 10
    raw_input = input("请输入一个正整数 n [直接回车默认 n=10]: ").strip()

    if not raw_input:
        n = 10
        print(f"未检测到输入，自动加载默认测试用例: n = {n}")
    else:
        try:
            n = int(raw_input)
        except ValueError:
            print("输入格式非有效整数，自动加载默认测试用例: n = 10")
            n = 10

    try:
        result = sum_factorial_reciprocals_fast(n)
        print(f"当 n = {n} 时，多项式之和为: {result:.10f}")
    except ValueError as err:
        print(f"计算失败: {err}")


if __name__ == "__main__":
    main()