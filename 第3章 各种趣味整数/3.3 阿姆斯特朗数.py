#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 阿姆斯特朗数 (Armstrong Numbers)

def is_armstrong_number(n: int) -> bool:
    """判断一个整数是否为阿姆斯特朗数。
    
    根据定义，如果一个整数等于其各个数位上数字的立方和，则该数称为阿姆斯特朗数。
    例如：153 = 1^3 + 5^3 + 3^3。

    Args:
        n (int): 待验证的整数。

    Returns:
        bool: 如果是阿姆斯特朗数则返回 True，否则返回 False。
    """
    if n <= 0:
        return False
        
    temp = n
    cube_sum = 0
    
    # 按从低位到高位的顺序，利用循环高效地拆分数位并直接累加立方和
    while temp > 0:
        digit = temp % 10
        cube_sum += digit ** 3
        temp //= 10
        
    return n == cube_sum


def main() -> None:
    """主函数，查找并格式化打印 1000 以内的所有阿姆斯特朗数。"""
    print("1000以内的阿姆斯特朗数: ")
    
    results = []
    # 遍历 2 到 999 之间的所有整数
    for i in range(2, 1000):
        if is_armstrong_number(i):
            results.append(str(i))
            
    # 使用制表符优雅地拼接输出结果，避免原代码末尾的多余空格
    print("\t".join(results))


if __name__ == "__main__":
    main()