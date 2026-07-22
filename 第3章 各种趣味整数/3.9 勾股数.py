#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @Time : 2019/6/12 0:37
# @desc: 勾股数  a**2+b**2=c**2

import math

def find_pythagorean_triples(limit: int = 100) -> list[tuple[int, int, int]]:
    """寻找指定上限范围内的所有勾股数（Pythagorean Triples）。

    勾股数满足 a^2 + b^2 = c^2，其中 1 <= a < b <= limit。
    采用完全整型的数学开方方式，避免了浮点数开方带来的精度误差风险。

    Args:
        limit (int): 直角边 a 和 b 的上限。默认为 100。

    Returns:
        list[tuple[int, int, int]]: 勾股数元组 (a, b, c) 的列表。
    """
    triples = []
    # a, b 分别表示直角三角形的两条直角边
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            sq_sum = a * a + b * b
            # 使用 Python 内置的纯整型开方，规避浮点数浮动带来的精度误差
            c = math.isqrt(sq_sum)
            
            # 判断是否是完全平方数（即符合 a^2 + b^2 = c^2）
            if c * c == sq_sum:
                # 三角形两边之和大于第三边（在正数前提下，勾股数性质天然保证 a + b > c，此处保留体现数学严谨性）
                if a + b > c:
                    triples.append((a, b, c))
    return triples


def main() -> None:
    """主入口函数。格式化打印勾股数列表（每行打印 4 组）。"""
    limit = 100
    print(f"{limit}以内的勾股数有: ")
    
    # 打印美观且列对齐的表头
    print("   a    b    c   \t|    a    b    c   \t|    a    b    c   \t|    a    b    c   \t|")
    print("-" * 85)
    
    triples = find_pythagorean_triples(limit)
    
    for idx, (a, b, c) in enumerate(triples, 1):
        # 格式化输出每组勾股数，保留统一的对齐宽度
        print(f"{a:4d} {b:4d} {c:4d}\t| ", end="")
        
        # 每输出 4 组换一次行
        if idx % 4 == 0:
            print()
            
    # 如果最后一物理行未填满 4 列，手动补充一个换行，确保终端排版整洁
    if len(triples) % 4 != 0:
        print()
        
    print(f"\n共找到 {len(triples)} 组满足条件的勾股数。")


if __name__ == '__main__':
    main()