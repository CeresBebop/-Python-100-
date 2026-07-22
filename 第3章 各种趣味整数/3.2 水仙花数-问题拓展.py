#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 水仙花数 (Narcissistic Number)

def is_narcissistic(n: int) -> bool:
    """判断一个三位数是否为水仙花数。

    水仙花数是指一个三位整数，其各位数字的立方和等于该数本身。
    例如：153 = 1^3 + 5^3 + 3^3。

    Args:
        n (int): 待判断的三位数。

    Returns:
        bool: 如果是水仙花数返回 True，否则返回 False。
    """
    if not (100 <= n <= 999):
        return False

    # 提取百位、十位和个位数字
    hun = n // 100
    ten = (n % 100) // 10  # 优化原有的 (n - hun * 100) // 10，直接使用模运算更高效直观
    ind = n % 10

    # 校验各位数的三次方之和是否等于原数
    return n == (hun**3 + ten**3 + ind**3)


def main() -> None:
    """遍历 100 到 999 之间的整数，检索并格式化输出所有水仙花数。"""
    print("result is: ")
    
    # 遍历所有三位数
    for n in range(100, 1000):
        if is_narcissistic(n):
            # 保留原代码使用制表符 '\t' 和空格间隔的输出风格，并升级为现代的 f-string 语法
            print(f"{n}\t", end=" ")
    print()  # 运行结束输出换行，保证终端格式整洁


if __name__ == '__main__':
    main()