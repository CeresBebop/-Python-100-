#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 黑洞数 (Kaprekar Constant / 卡普雷卡尔黑洞数)

def get_three_max(a: int, b: int, c: int) -> int:
    """获取三个数字组合成的最大三位数。

    将输入的三个数字降序排列并组合成一个三位数。例如：输入 4, 9, 5 返回 954。

    Args:
        a (int): 数字一。
        b (int): 数字二。
        c (int): 数字三。

    Returns:
        int: 组合成的最大三位数。
    """
    # 使用 Python 内置的高效排序算法，完全替代原书冗长且容易出错的手写冒泡排序
    digits = sorted([a, b, c], reverse=True)
    return digits[0] * 100 + digits[1] * 10 + digits[2]


def get_three_min(a: int, b: int, c: int) -> int:
    """获取三个数字组合成的最小三位数。

    将输入的三个数字升序排列并组合成一个三位数。例如：输入 4, 9, 5 返回 459。

    Args:
        a (int): 数字一。
        b (int): 数字二。
        c (int): 数字三。

    Returns:
        int: 组合成的最小三位数。
    """
    # 升序排列
    digits = sorted([a, b, c])
    return digits[0] * 100 + digits[1] * 10 + digits[2]


def find_black_number(initial_max: int, initial_min: int) -> None:
    """计算并输出三位数的黑洞数（卡普雷卡尔常数 495 的迭代验证过程）。

    该函数通过数位拆分、重排求差的循环迭代，引导任意非完全相同数字的三位数收敛到 495。

    Args:
        initial_max (int): 初始的最大排列值。
        initial_min (int): 初始的最小排列值。
    """
    # 修复原书参数名覆盖 Python 内置函数 max/min 的代码规范缺陷
    j = initial_max - initial_min
    k = 0
    
    # 设定合理的迭代上限。数学上，3位卡普雷卡尔常数最多在 6 次迭代内必收敛。
    # 原书中的 "while k < min" 是一个非常困惑且危险的循环终止条件（因为 min 往往是一个很大的数值如 459），
    # 这里优化为基于最大迭代步数（安全限额 10 次）的安全循环。
    while k < 10:
        h = j
        hun = j // 100
        ten = (j % 100) // 10
        bit = j % 10
        
        curr_max = get_three_max(hun, ten, bit)
        curr_min = get_three_min(hun, ten, bit)
        j = curr_max - curr_min
        
        # 如果连续两次迭代的结果相同，说明已成功收敛到黑洞数
        if j == h:
            print(f"黑洞数为: {j}")
            break
        k += 1


def main() -> None:
    """主入口函数。安全获取用户输入，验证合法性并启动黑洞数迭代算法。"""
    try:
        user_input = input("请输入一个三位整数（各个数位数字不能完全相同，回车默认 351）：").strip()
        # 提供默认的合法测试值，以支持免配置直接一键运行
        num = int(user_input) if user_input else 351

        if not (100 <= num <= 999):
            print("输入错误：必须输入 100 到 999 之间的三位整数！")
            return
        
        # 数位拆分
        hun = num // 100
        ten = (num % 100) // 10
        bit = num % 10

        # 数学逻辑前置拦截：三个数字完全相同（如 111）在运算时无意义（差值为0）
        if hun == ten == bit:
            print("输入提示：三位数各数位完全相同（如 111）时，差值为 0，黑洞数为: 0")
            return

        max_val = get_three_max(hun, ten, bit)
        min_val = get_three_min(hun, ten, bit)
        
        print(f"重组最大值 max = {max_val}")
        print(f"重组最小值 min = {min_val}")
        
        find_black_number(max_val, min_val)

    except ValueError:
        print("输入错误：请输入有效的整数")


if __name__ == '__main__':
    main()