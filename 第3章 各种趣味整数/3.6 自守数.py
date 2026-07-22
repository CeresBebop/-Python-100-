#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 自守数 (Automorphic Numbers)

import math

def is_automorphic_pythonic(number: int) -> bool:
    """采用极其高效且易读的数学取模法判断一个数是否为自守数。

    自守数是指一个数的平方的尾数等于该数自身的自然数。
    在 Python 中，由于支持任意精度整数（无溢出风险），可以直接计算平方并通过 10 的幂进行尾数截取，
    这比原代码中模拟手算乘法的逐位累加法在运行速度和可读性上有了质的飞跃。

    Args:
        number (int): 待判断的自然数。

    Returns:
        bool: 如果是自守数返回 True，否则返回 False。
    """
    if number == 0:
        return True
        
    # 数学方法：计算当前数字的位数
    # 例如：376 有 3 位，对应的截取模数为 10^3 = 1000
    digits = int(math.log10(number)) + 1
    modulus = 10 ** digits
    
    # 判断平方的尾数是否等于原数自身
    return (number ** 2) % modulus == number


def is_automorphic_partial_products(number: int) -> bool:
    """自守数的核心手算模拟算法（保留并完美还原了原书的算法设计）。

    该方法模拟了手工乘法（部分积累加）的过程：通过截取被乘数与乘数的对应数位，
    只计算那些对最终尾数有贡献的部分积，并将累加值限制在当前数位的模数以内。
    这在低级语言（如 C/C++）中是为了防止大数平方直接计算溢出而设计的经典算法。

    Args:
        number (int): 待判断的自然数。

    Returns:
        bool: 如果是自守数返回 True，否则返回 False。
    """
    if number == 0:
        return True

    # 1. 计算数字的最高位系数 k
    mul = number
    k = 1
    while (mul // 10) > 0:
        mul //= 10
        k *= 10

    # 2. 核心迭代：逐步累加对尾数有影响的部分积并进行截断
    a = k * 10
    mul = 0
    b = 10
    temp_k = k
    while temp_k > 0:
        # (部分积 + 截取被乘数的后 N 位 * 截取乘数的第 M 位) % a
        # 完美补全并还原了原书被截断的公式：
        digit_m = number % b - number % (b // 10)
        mul = (mul + (number % (temp_k * 10)) * digit_m) % a
        temp_k //= 10
        b *= 10

    return number == mul


def main() -> None:
    """主程序入口，遍历 100000 以内的数字，查找并优雅地打印所有自守数。"""
    print("100000以内的自守数: ")
    
    results = []
    # 遍历范围 [0, 99999]
    for number in range(0, 100000):
        # 此处使用性能极优的 pythonic 算法进行查找，
        # 您可以无缝替换为 is_automorphic_partial_products(number) 验证其等价性
        if is_automorphic_pythonic(number):
            results.append(str(number))
            
    # 按制表符分隔优雅输出
    print("\t".join(results))


if __name__ == "__main__":
    main()