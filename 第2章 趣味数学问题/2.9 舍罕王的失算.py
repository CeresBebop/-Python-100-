#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 舍罕王的失算

def calculate_grains_loop() -> int:
    """使用循环方式精确计算国王总共需要赏赐的麦子数。

    通过整型(int)累加避免浮点数精度丢失，且用乘 2 递推代替 2**(i-1) 幂运算，提高效率。

    Returns:
        int: 麦子总粒数
    """
    total_grains = 0
    current_grains = 1  # 棋盘第 1 格放 1 粒麦子
    for _ in range(64):
        total_grains += current_grains
        current_grains *= 2  # 下一格麦子数翻倍，比重算 2**(i-1) 效率高得多
    return total_grains


def calculate_grains_math() -> int:
    """使用等比数列求和公式直接计算总麦子数。

    公式：Sum = 2^0 + 2^1 + ... + 2^63 = 2^64 - 1
    利用位左移操作 (1 << 64) - 1 达到极致的 O(1) 效率。

    Returns:
        int: 麦子总粒数
    """
    return (1 << 64) - 1


if __name__ == "__main__":
    print("=" * 60)
    print("【舍罕王的失算】 麦粒精确计算程序")
    print("=" * 60)

    # 1. 精确计算总麦粒数（使用 O(1) 极致公式）
    grains = calculate_grains_math()
    
    print("1. 棋盘 64 格上麦子的精确总粒数：")
    print(f"   {grains} 粒")
    print()
    
    # 2. 现实物理量化评估（让“失算”更加直观）
    # 假设每 25,000 粒麦子重 1 公斤 (即单粒麦子重约 0.04 克)
    GRAINS_PER_KG = 25000
    weight_kg = grains / GRAINS_PER_KG
    weight_tons = weight_kg / 1000
    
    # 目前全球小麦年总产量大约为 7.5 亿吨
    GLOBAL_ANNUAL_WHEAT_PRODUCTION_TONS = 750_000_000
    years_needed = weight_tons / GLOBAL_ANNUAL_WHEAT_PRODUCTION_TONS
    
    print("2. 现实量化换算：")
    print(f"   - 麦子总重量约： {weight_kg:,.2f} 公斤 (kg)")
    print(f"   - 折合吨数约为： {weight_tons:,.2f} 吨 (t)")
    print(f"   - 以目前全球小麦年产量（约 7.5 亿吨）估算，")
    print(f"     国王需要不吃不喝收割全地球的小麦约 {years_needed:.1f} 年，才能兑现他的诺言！")
    print("=" * 60)