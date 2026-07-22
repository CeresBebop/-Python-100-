#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 回文数


def check_five_digit_palindrome(x: int) -> bool:
    """验证一个5位数是否为回文数。

    通过数学的整除和取余运算提取各个数位上的数字，
    比较万位与个位、千位与十位是否对应相等。

    Args:
        x (int): 待验证的5位整数。

    Returns:
        bool: 如果是5位回文数则返回 True，否则返回 False。

    Raises:
        ValueError: 当输入的数字不是5位数时抛出。
    """
    # 严格限定范围：5位数必须在 10000 到 99999 之间
    if not (10000 <= x <= 99999):
        raise ValueError("输入错误")

    # 提取万位数字
    ten_thousand = x // 10000
    # 提取千位数字
    thousand = (x % 10000) // 1000
    # 提取十位数字
    ten = (x % 100) // 10
    # 提取个位数字
    indiv = x % 10

    # 判断回文条件：个位等于万位 且 十位等于千位（百位无需比对）
    return indiv == ten_thousand and ten == thousand


def main() -> None:
    """主函数，负责安全地获取用户输入并调用验证逻辑。"""
    try:
        user_input = input("请输入一个5位数整数: ")
        x = int(user_input)

        if check_five_digit_palindrome(x):
            print(f"{x}是回文数")
        else:
            print(f"{x}不是回文数")

    except ValueError as e:
        # 捕获输入非整数时的 ValueError，或 check_five_digit_palindrome 抛出的范围错误
        if str(e) == "输入错误":
            print("输入错误")
        else:
            print("输入错误")  # 统一处理非整数字符串输入，避免程序崩溃


if __name__ == "__main__":
    main()