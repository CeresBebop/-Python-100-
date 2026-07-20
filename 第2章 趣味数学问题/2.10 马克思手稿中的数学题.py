#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 马克思手稿中的数学题

def solve_marx_problem(allow_zero: bool = False) -> None:
    """求解马克思手稿中的经典数学题，并以美观的表格形式输出。

    问题描述：
    有 30 个人（包含男人、女人和小孩）在饭馆吃饭共花了 50 先令。
    每个男人花 3 先令，每个女人花 2 先令，每个小孩花 1 先令。
    问男人、女人和小孩各几人？

    数学建模：
    设男人为 x 人，女人为 y 人，小孩为 z 人：
    1) x + y + z = 30
    2) 3x + 2y + z = 50
    
    由方程组消元化简直接可得：
    y = 20 - 2x
    z = 10 + x

    Args:
        allow_zero (bool): 是否允许某些人群人数为 0。
                           若为 False（默认），表示必须同时有男人、女人和小孩（x, y, z >= 1）；
                           若为 True，允许某类人数为 0（x, y, z >= 0）。
    """
    # 确定输出标题
    constraint_desc = "（要求三类人群必须同时存在）" if not allow_zero else "（允许某类人群人数为 0）"
    print(f"\n马克思手稿数学题求解结果 {constraint_desc}")
    print("=" * 55)
    # 格式化表头，确保中英文对齐美观
    print(f"{'方案 (No.)':^10} | {'男人 (Men)':^10} | {'女人 (Women)':^12} | {'小孩 (Children)':^14}")
    print("-" * 55)

    number = 0
    # 根据 y = 20 - 2x >= 0，推导出 x 的最大理论取值范围为 0 到 10
    for x in range(0, 11):
        y = 20 - 2 * x
        z = 10 + x
        
        # 物理意义约束条件过滤
        if allow_zero:
            # 允许人数为 0 的宽泛情况
            is_valid = (x >= 0 and y >= 0 and z >= 0)
        else:
            # 严格符合“有男人、女人和小孩”的字面实际意义
            is_valid = (x >= 1 and y >= 1 and z >= 1)
            
        if is_valid:
            number += 1
            # 使用 f-string 进行优雅、居中对齐的表格输出
            print(f"{number:^10} | {x:^10} | {y:^12} | {z:^14}")

    print("=" * 55)


if __name__ == "__main__":
    # 1. 严格解：三类人必须同时存在（最符合“有男人、女人和小孩”的实际物理语义）
    solve_marx_problem(allow_zero=False)
    
    # 2. 宽泛解：允许某类人群数量为 0
    solve_marx_problem(allow_zero=True)