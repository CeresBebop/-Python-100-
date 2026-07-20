#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @desc: 换分币

def exchange_coins(total_jiao: int = 50) -> None:
    """计算将指定金额（单位：角）兑换为 1元、5角和 1角硬币的所有可能组合。

    数学建模：
    10 * A + 5 * B + 1 * C = total_jiao
    其中：
    - A 代表 1 元硬币数量（面值为 10 角）
    - B 代表 5 角硬币数量（面值为 5 角）
    - C 代表 1 角硬币数量（面值为 1 角）

    Args:
        total_jiao (int): 待兑换的总钱数（角）。默认为 50 角（即 5 元）。
    """
    count = 0
    print(f"【兑换目标】：将 {total_jiao / 10:.1f} 元（{total_jiao}角）兑换为 1元、5角和 1角硬币")
    print("=" * 110)
    print("可能的兑换方法如下（每行显示 3 种方案）：\n")

    # 外层循环：1 元硬币占用的钱数 x（每张 1 元等于 10 角，步长为 10）
    for x in range(0, total_jiao + 1, 10):
        # 中层循环：5 角硬币占用的钱数 y（每张 5 角等于 5 角，步长为 5）
        for y in range(0, total_jiao - x + 1, 5):
            # 算法优化：1 角硬币占用的钱数 z 已经由 x 和 y 唯一确定，无需第三层循环
            z = total_jiao - x - y
            
            count += 1
            
            # 计算对应的硬币数量
            num_1yuan = x // 10
            num_5jiao = y // 5
            num_1jiao = z
            
            # 使用 f-string 配合格式化占位符，保证高可读性的标准列宽
            solution_str = f"方案 {count:2d}: 10 * {num_1yuan} + 5 * {num_5jiao} + 1 * {num_1jiao:<2d}"
            
            # 实现每 3 列换行一次的网格布局
            if count % 3 == 0:
                print(f"{solution_str:<32}")
            else:
                print(f"{solution_str:<32}", end="  |  ")

    # 如果总方案数不是 3 的倍数，在结尾补充换行
    if count % 3 != 0:
        print()
        
    print("\n" + "=" * 110)
    print(f"【计算结果】：共计有 {count} 种不同的兑换方法。")
    print("=" * 110)


if __name__ == "__main__":
    # 执行 5 元钱（50 角）的换币方案计算
    exchange_coins(total_jiao=50)