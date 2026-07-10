#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop (Modified)
# @desc: 数制转换

# 将字符转换成数字（支持0-9和A-Z）
def char_to_num(ch):
    ch = ch.upper() # 统一转换为大写字母
    if '0' <= ch <= '9':
        return int(ch)
    elif 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 10
    else:
        raise ValueError(f"非法字符: {ch}")

# 将数字转换为字符（支持0-9和A-Z）
def num_to_char(num):
    if 0 <= num <= 9:
        return str(num)
    elif 10 <= num <= 35:
        return chr(num - 10 + ord('A'))
    else:
        raise ValueError(f"超出进制表示范围的数字: {num}")

# 其他数制转换为十进制 
def source_to_decimal(temp, source):
    decimal_num = 0
    for i in range(len(temp)):
        decimal_num = (decimal_num * source) + char_to_num(temp[i])
    return decimal_num

# 十进制转换为其他数制
def decimal_to_object(decimal_num, target_base):
    if decimal_num == 0:
        return ['0']
        
    result_chars = []
    while decimal_num > 0:
        # 使用 % 取余，适用于所有进制
        remainder = decimal_num % target_base
        result_chars.append(num_to_char(remainder))
        decimal_num //= target_base # 用十进制数整除以基数

    return result_chars

# 逆序输出余数数组
def output(decimal_list):
    f = len(decimal_list) - 1
    while f >= 0:
        print(decimal_list[f], end='')
        f -= 1
    print()

if __name__ == "__main__":
    flag = 1 
    while flag: 
        print('转换前的数是: ', end='')
        temp = input().strip()
        
        print("转换前的数制是: ", end='')
        source = int(input())
        
        print("转换后的数制是: ", end='')
        target_base = int(input())  # 修复：原代码遗漏了输入目标数制
        
        print("转换后的数是: ", end='')
        # 1. 先转十进制
        decimal_num = source_to_decimal(temp, source)
        # 2. 再由十进制转目标进制
        target_list = decimal_to_object(decimal_num, target_base)
        # 3. 打印结果
        output(target_list)
        
        print("请继续输入1, 否则输入0: ")
        try:
            flag = int(input())
        except ValueError:
            flag = 0