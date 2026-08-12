#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 多项式之和 (计算 S = 1/1! + 1/2! + 1/3! + ... + 1/n!)


def sum_factorial_reciprocals(n: int) -> float:
    """计算多项式之和 S = 1/1! + 1/2! + 1/3! + ... + 1/n!。

    算法逻辑（方法1）：
    通过双重循环分别计算每一项 i 的阶乘 i!，再将其倒数 1/i! 累加至总和中。

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
    i = 1

    # 外层循环：控制多项式累加项数 1 ~ n
    while i <= n:
        t = 1
        j = 1
        # 内层循环：计算第 i 项的阶乘 t = i!
        while j <= i:
            t = t * j
            j += 1

        # 累加当前项倒数 1/t
        s = s + 1.0 / t
        i += 1

    return s


def main() -> None:
    """主程序入口，包含交互输入与零配置默认回退机制。"""
    print("=== 多项式之和计算程序 (S = 1/1! + 1/2! + ... + 1/n!) ===")

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
        result = sum_factorial_reciprocals(n)
        print(f"当 n = {n} 时，多项式之和为: {result:.10f}")
    except ValueError as err:
        print(f"计算失败: {err}")


if __name__ == "__main__":
    main()