#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 回文数 (寻找 1-255 之间，其平方数为回文数的数字)

def is_palindrome(num: int) -> bool:
    """判断一个整数是否为回文数。
    
    采用数学方法（取模与整除）重建逆序数字，避免了数组越界风险，
    比原代码中使用的固定长度数组重建法更加高效、安全且符合 Pythonic 风格。

    Args:
        num (int): 需要判断的待测整数。

    Returns:
        bool: 如果是回文数返回 True，否则返回 False。
    """
    if num < 0:
        return False
    
    original = num
    reversed_num = 0
    
    # 通过循环，每次提取最低位数字并累加到逆序变量中
    while num > 0:
        digit = num % 10          # 获取当前最低位数字
        reversed_num = reversed_num * 10 + digit  # 将该数字拼接到逆序结果的末尾
        num //= 10                # 去掉已处理的最低位
        
    return original == reversed_num


def find_palindromic_squares(limit: int = 256) -> None:
    """寻找在指定范围内其平方值为回文数的数字，并格式化输出结果。

    Args:
        limit (int): 遍历范围的上限（不包含该值）。默认值为 256。
    """
    count = 0
    # 格式化打印表头，确保列对齐美观
    print(f"{'No.':<6}{'Number':<12}{'Square (Palindrome)'}")
    print("-" * 38)
    
    for n in range(1, limit):
        square = n * n
        # 判断当前数字的平方是否是回文数
        if is_palindrome(square):
            count += 1
            # 优雅对齐输出序号、原数以及其平方值
            print(f"{count:<6d}{n:<12d}{square:<d}")


if __name__ == '__main__':
    find_palindromic_squares()