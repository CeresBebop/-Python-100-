#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 水仙花数 (Narcissistic Number)

def is_narcissistic_number(n: int) -> bool:
    """判断一个三位数是否为水仙花数。
    
    水仙花数是指一个三位数，其各位数字的立方和等于该数本身。
    例如：153 = 1^3 + 5^3 + 3^3。

    Args:
        n (int): 待验证的三位整数。

    Returns:
        bool: 如果是水仙花数则返回 True，否则返回 False。
    """
    if not (100 <= n <= 999):
        return False
        
    # 使用 Python 内置的 divmod 函数一步到位、高效地分离出百位、十位和个位
    hun, temp = divmod(n, 100)   # hun 为百位，temp 为十位和个位组成的余数
    ten, ind = divmod(temp, 10)  # ten 为十位，ind 为个位
    
    # 计算各位数的三次方之和
    cube_sum = hun**3 + ten**3 + ind**3
    
    return n == cube_sum


def find_narcissistic_numbers() -> None:
    """遍历 100 到 999 之间的所有整数，查找并优雅地输出所有水仙花数。"""
    print("result is: ")
    results = []
    
    # 整数的取值范围：100 到 999
    for n in range(100, 1000):
        if is_narcissistic_number(n):
            results.append(str(n))
            
    # 使用制表符 \t 拼接结果，避免原代码在循环尾部输出多余空格和制表符的问题
    print("\t".join(results))


if __name__ == '__main__':
    find_narcissistic_numbers()