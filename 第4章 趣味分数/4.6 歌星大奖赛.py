#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 歌星大奖赛 - 评委打分（去掉一个最高分、去掉一个最低分求平均得分）

import sys


def calculate_competition_score(
    scores: list[float],
) -> tuple[float, float, float]:
    """根据评委打分列表计算最高分、最低分和最终平均得分。

    计算规则：
    1. 找出所有打分中的最高分和最低分。
    2. 去掉一个最高分和一个最低分。
    3. 计算剩余评委打分的平均分。

    Args:
        scores (list[float]): 评委打分列表 (要求至少 3 个打分)

    Returns:
        tuple[float, float, float]: (最高分, 最低分, 最终平均得分)

    Raises:
        ValueError: 当评委打分数量少于 3 个时抛出
    """
    if len(scores) < 3:
        raise ValueError("评委打分数量必须至少为 3 个才能计算去掉极值后的平均分")

    # 避开内置函数名遮蔽
    max_score = max(scores)
    min_score = min(scores)
    total_sum = sum(scores)

    # 扣除一个最高分和一个最低分后求平均分（精确浮点运算）
    final_score = (total_sum - max_score - min_score) / (len(scores) - 2)

    return max_score, min_score, final_score


def main() -> None:
    """主程序入口，支持交互式输入与零配置默认回退逻辑。"""
    print("=== 歌星大奖赛评委打分系统 ===")
    num_judges = 10
    default_scores = [90.0, 95.0, 88.0, 92.0, 100.0, 85.0, 96.0, 94.0, 91.0, 89.0]

    raw_input = input(
        f"请输入 {num_judges} 个评委打分 (0-100分，空格分隔) [直接回车默认加载模拟打分]: "
    ).strip()

    scores = []

    # 零配置容错处理：若无输入或按回车，自动加载默认测试用例
    if not raw_input:
        scores = default_scores
        print(f"未检测到输入，自动加载默认测试用例: {scores}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != num_judges:
                print(f"输入的打分数量不为 {num_judges} 个，切换为默认打分演示。")
                scores = default_scores
            else:
                for idx, p in enumerate(parts, start=1):
                    score = float(p)
                    if score < 0 or score > 100:
                        raise ValueError(f"第 {idx} 个评委分数 ({score}) 超出 0~100 范围")
                    scores.append(score)
        except ValueError as err:
            print(f"输入格式解析错误 ({err})，自动加载默认测试打分。")
            scores = default_scores

    print("\n----- 评委打分详情 -----")
    for idx, score in enumerate(scores, start=1):
        print(f"第 {idx:2d} 个评委打分: {score:g}")

    # 计算最终得分
    max_score, min_score, final_score = calculate_competition_score(scores)

    print("\n----- 最终统计结果 -----")
    print(f"去掉一个最高分: {max_score:g}")
    print(f"去掉一个最低分: {min_score:g}")
    print(f"最后得分: {final_score:.2f}")


if __name__ == "__main__":
    main()