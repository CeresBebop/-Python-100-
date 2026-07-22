#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 阿姆斯特朗数 (从高位到低位拆分)

def extract_digits_high_to_low(n: int) -> list[int]:
    """按从高位到低位的顺序拆分一个正整数的各个数位。

    该算法采用纯数学运算，通过动态计算最高位除数，依次提取每位数字，
    彻底解决了原代码无法适配不同位数（硬编码范围）的局限性。

    Args:
        n (int): 需要拆分的正整数。

    Returns:
        list[int]: 拆分后的数字列表（高位在前，低位在后）。
    """
    if n == 0:
        return [0]
        
    digits = []
    # 动态寻找当前数字最高位的除数基准（例如输入 153 时，最高位除数为 100）
    divisor = 1
    while divisor * 10 <= n:
        divisor *= 10
        
    # 从高位向低位依次提取每一位上的数字并移位
    temp = n
    while divisor > 0:
        digit = temp // divisor
        digits.append(digit)
        temp %= divisor
        divisor //= 10
        
    return digits


def is_armstrong_number(n: int) -> bool:
    """判断一个数是否为阿姆斯特朗数。
    
    阿姆斯特朗数定义为其各个数位的立方和等于该数本身。

    Args:
        n (int): 待判断的整数。

    Returns:
        bool: 如果是阿姆斯特朗数则返回 True，否则返回 False。
    """
    # 提取数位
    digits = extract_digits_high_to_low(n)
    
    # 计算立方和（使用内置 sum() 与列表推导式，避免硬编码索引和内置函数覆盖）
    cube_sum = sum(d ** 3 for d in digits)
    
    return n == cube_sum


def main() -> None:
    """主程序入口，遍历 2 到 999 并整洁地输出阿姆斯特朗数。"""
    print("1000以内的阿姆斯特朗数: ")
    results = []
    
    for i in range(2, 1000):
        if is_armstrong_number(i):
            results.append(str(i))
            
    # 使用制表符拼装，规范输出排版
    print("\t".join(results))


if __name__ == '__main__':
    main()