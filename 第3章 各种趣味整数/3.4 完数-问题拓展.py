#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 完数 (优化搜索空间版本)

def is_perfect_number(i: int) -> bool:
    """通过将真因子搜索范围缩小至 i // 2 来判断一个数是否为完数。

    根据数学原理，任何整数的最大真因子（除自身外）都不可能超过其自身的一半 (i // 2)。
    因此，将循环范围缩减至 [1, i // 2]，不仅使计算量比全遍历减半，且逻辑上完全正确。

    Args:
        i (int): 待判断的整数。

    Returns:
        bool: 如果是完数返回 True，否则返回 False。
    """
    if i <= 1:
        return False
        
    s = 0
    # 精确检索区间 [1, i // 2] 内的因子，最大因子不可能超过自身的一半
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            s += j
            
    return s == i


def main() -> None:
    """主程序，安全获取上限输入并查找打印完数。"""
    try:
        user_input = input("请输入所选范围上限（回车默认 1000）：").strip()
        n = int(user_input) if user_input else 1000
        
        if n < 2:
            print("输入错误：上限必须不小于 2")
            return

        print(f"正在寻找 2 到 {n} 之间的完数...")
        
        perfect_numbers_found = False
        for i in range(2, n + 1):
            if is_perfect_number(i):
                perfect_numbers_found = True
                # 规范化输出格式
                print(f"2到{n}之间的完数: {i}")
                
        if not perfect_numbers_found:
            print("未找到任何完数。")

    except ValueError:
        print("输入错误：请输入有效的整数")


if __name__ == "__main__":
    main()