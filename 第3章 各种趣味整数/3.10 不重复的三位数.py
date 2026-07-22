#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 不重复的3位数

from itertools import permutations

def find_unique_three_digit_numbers() -> list[int]:
    """使用 itertools.permutations 高效生成由 1, 2, 3, 4 组成的无重复数字的三位数。

    采用 Python 官方标准库自带的排列组合迭代器，比传统的三层嵌套循环具备更佳的
    可读性与算法扩展性，并在底层实现非重复过滤，执行效率极高。

    Returns:
        list[int]: 生成的所有不重复三位数的列表。
    """
    digits = [1, 2, 3, 4]
    unique_numbers = []
    
    # permutations(digits, 3) 直接生成所有长度为 3 且元素不重复的元组排列
    for perm in permutations(digits, 3):
        # 拆包元组并还原为三位整数。例如：(1, 2, 3) -> 123
        num = perm[0] * 100 + perm[1] * 10 + perm[2]
        unique_numbers.append(num)
        
    return unique_numbers


def main() -> None:
    """主入口函数。调用算法生成所有组合，并每行 8 个数格式化输出。"""
    print("由1、2、3、4组成的互不相同且无重复数字的三位数有：")
    print("-" * 52)
    
    unique_numbers = find_unique_three_digit_numbers()
    count = len(unique_numbers)
    
    for idx, num in enumerate(unique_numbers, 1):
        # 现代化 f-string 排版，左对齐并预留 6 位字符宽度确保绝对工整
        print(f"{num:<6d}", end="")
        
        # 每输出 8 个数字自动换行
        if idx % 8 == 0:
            print()
            
    # 确保最后一物理行输出完毕后换行
    if count % 8 != 0:
        print()
        
    print("-" * 52)
    print(f"三位互不相同的数，共有: {count} 个")


if __name__ == '__main__':
    main()