#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 高次方数的尾数 (Last Three Digits of High Power Numbers)

def power_modulo(x: int, y: int, mod: int = 1000) -> int:
    """采用快速幂算法高效计算 (x^y) % mod 的值。

    将时间复杂度由原代码的 O(y) 优化至 O(log y)。
    当指数 y 极大（如百万、亿级别）时，能瞬间得出答案，避免了原书简单循环导致的程序超时和假死。

    Args:
        x (int): 底数。
        y (int): 指数（必须非负）。
        mod (int): 模数。默认为 1000（即提取尾部三位数字）。

    Returns:
        int: 计算得到的尾数。
    """
    if y < 0:
        raise ValueError("指数 y 必须非负")
        
    res = 1
    x = x % mod
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % mod
        y //= 2
        x = (x * x) % mod
    return res


def main() -> None:
    """主入口函数。安全获取用户输入，计算并优雅输出高次方数的后三位尾数。"""
    try:
        print("请输入两个数x和y: ")
        x_input = input("x = ").strip()
        y_input = input("y = ").strip()
        
        # 兼容空输入，提供默认模拟数据以便在 VS Code 中一键直接运行而不会崩溃
        x = int(x_input) if x_input else 13
        y = int(y_input) if y_input else 13

        if y < 0:
            print("输入错误：指数 y 必须是非负整数")
            return

        # 优化方案一：手写快速幂算法 (时间复杂度 O(log y))
        last_manual = power_modulo(x, y, 1000)
        
        # 优化方案二：使用 Python 底层内置快速幂函数 pow(x, y, 1000)
        last_builtin = pow(x, y, 1000)

        # 细节体验优化：尾数（后三位）很可能包含前导零（例如 1001^3 尾数应为 "001"），
        # 原书直接使用 %d 会导致 "001" 被错印成 "1"。这里采用 :03d 格式化补齐前导零。
        print(f"\n[快速幂算法] {x} 的 {y} 次方所得积的后三位为: {last_manual:03d}")
        print(f"[内置pow函数] {x} 的 {y} 次方所得积的后三位为: {last_builtin:03d}")

    except ValueError:
        print("输入错误：请输入有效的整数")


if __name__ == '__main__':
    main()