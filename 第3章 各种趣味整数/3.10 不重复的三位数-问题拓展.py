#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 不重复的3位数 (分支剪枝优化版)

def find_unique_three_digit_numbers_optimized() -> list[int]:
    """生成由 1, 2, 3, 4 组成的无重复数字的三位数。

    采用分支剪枝（Pruning）优化：在第二层循环中，如果发现第一位数字 i 与第二位数字 j 相等，
    则直接使用 continue 跳过第三位数字 k 的多余遍历。这一方法极大减少了冗余循环建立。

    Returns:
        list[int]: 生成的所有不重复三位数的列表。
    """
    unique_numbers = []
    
    # 第一位数字
    for i in range(1, 5):
        # 第二位数字
        for j in range(1, 5):
            # 核心剪枝优化：如果前两位数字已经重复，直接跳过第三位数字的遍历。
            # 这比原书中使用 while 循环手动管理 k 的指针更符合 Pythonic 规范，执行效率更高。
            if i == j:
                continue
            
            # 第三位数字
            for k in range(1, 5):
                if k != i and k != j:
                    num = i * 100 + j * 10 + k
                    unique_numbers.append(num)
                    
    return unique_numbers


def main() -> None:
    """主入口函数。执行生成算法并格式化每行打印 8 个数字。"""
    print("由1、2、3、4组成的互不相同且无重复数字的三位数（剪枝优化版）有：")
    print("-" * 52)
    
    unique_numbers = find_unique_three_digit_numbers_optimized()
    count = len(unique_numbers)
    
    for idx, num in enumerate(unique_numbers, 1):
        # 使用 f-string 的 :<6d 保证数字左对齐且间隔绝对对称
        print(f"{num:<6d}", end="")
        
        # 每 8 个数字换行一次
        if idx % 8 == 0:
            print()
            
    # 收尾换行，保证终端格式整齐
    if count % 8 != 0:
        print()
        
    print("-" * 52)
    print(f"三位互不相同的数，共有: {count} 个")


if __name__ == '__main__':
    main()