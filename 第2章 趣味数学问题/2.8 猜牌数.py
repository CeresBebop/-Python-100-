#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 猜牌术 (魔术师翻牌问题)

def solve_card_trick() -> list[int]:
    """使用环形列表与模运算，模拟魔术师猜牌术。

    算法原理：
    - 桌上有 13 个空位排成一圈，用 0 代表空盒子。
    - 依次放入牌 1 到 13。对于牌 i，需要从当前位置向后数出 i 个空盒子，并在第 i 个空盒子处放入牌 i。
    - 指针移到下一位，继续下一张牌的循环放置。

    Returns:
        list[int]: 13张牌从最上面到最底部的原始排列顺序（数值 1-13 分别代表 A-K）
    """
    # 初始化 13 个盒子（0 代表当前为空）
    cards = [0] * 13
    current_pos = 0  # 初始指针位置（0-indexed）

    for card_val in range(1, 14):
        empty_count = 0  # 记录当前已数过的空盒子数量
        while empty_count < card_val:
            # 只有当盒子为空时，才算作有效计步
            if cards[current_pos] == 0:
                empty_count += 1
                # 数到第 card_val 个空盒子时，将牌放入
                if empty_count == card_val:
                    cards[current_pos] = card_val
            
            # 指针向后移一位。通过模 13 运算实现闭环循环，优雅且绝对安全，消除了溢出风险。
            current_pos = (current_pos + 1) % 13

    return cards


def format_spade_card(val: int) -> str:
    """将数字牌面转换为更直观、高表现力的扑克牌黑桃格式。

    Args:
        val (int): 扑克牌数值 (1-13)

    Returns:
        str: 带有黑桃符号的扑克牌面（如 ♠A, ♠10, ♠K）
    """
    card_map = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    face = card_map.get(val, str(val))
    return f"♠{face}"


if __name__ == '__main__':
    print("=" * 60)
    print("【魔术师猜牌术】原始牌序求解程序")
    print("=" * 60)
    
    # 1. 运行核心算法求解原始牌序
    original_order = solve_card_trick()
    
    # 2. 打印原始数值列表（对应原书 a[1:] 格式要求）
    print("1. 原始数值顺序 (1-13 分别对应 A-K):")
    print(original_order)
    print()
    
    # 3. 打印视觉增强版牌面顺序（极大地提升了用户体验）
    print("2. 视觉增强版原始牌序 (从上到下顺序):")
    formatted_cards = [format_spade_card(x) for x in original_order]
    print(" -> ".join(formatted_cards))
    print("=" * 60)