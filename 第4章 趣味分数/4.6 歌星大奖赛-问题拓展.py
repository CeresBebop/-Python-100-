#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 歌星大奖赛 - 评委打分综合分析 (含最高/最低分、最终得分、最公平/最不公平评委评定)

import random


def analyze_competition_scores(scores: list[float]) -> dict:
    """分析评委打分数据，计算最终得分、最公平评委和最不公平评委。

    评定标准：
    1. 扣除一个最高分和一个最低分后，求剩余打分的精确平均值。
    2. 最公平评委：其打分与最终平均分的绝对偏差最小 |score - avg|。
    3. 最不公平评委：其打分与最终平均分的绝对偏差最大 |score - avg|。

    Args:
        scores (list[float]): 10 位评委的打分列表

    Returns:
        dict: 包含打分统计分析结果的字典
    """
    n = len(scores)
    max_val = max(scores)
    min_val = min(scores)

    # 去掉一个最高分和一个最低分后的平均得分（浮点数精准计算）
    total_sum = sum(scores)
    trimmed_sum = total_sum - max_val - min_val
    avg_score = trimmed_sum / (n - 2)

    # 计算各评委打分与平均分的绝对偏差距离
    diffs = [abs(s - avg_score) for s in scores]
    min_diff = min(diffs)
    max_diff = max(diffs)

    # 寻找偏差最小（最公平）与偏差最大（最不公平）的评委编号（1-based）和打分
    most_fair_judges = [
        (i + 1, scores[i])
        for i, diff in enumerate(diffs)
        if abs(diff - min_diff) < 1e-9
    ]
    most_unfair_judges = [
        (i + 1, scores[i])
        for i, diff in enumerate(diffs)
        if abs(diff - max_diff) < 1e-9
    ]

    return {
        "scores": scores,
        "max_score": max_val,
        "min_score": min_val,
        "avg_score": avg_score,
        "most_fair": most_fair_judges,
        "most_unfair": most_unfair_judges,
    }


def main() -> None:
    """主程序入口，自动生成符合实际的评委打分并打印综合分析报告。"""
    print("=== 歌星大奖赛评委打分综合分析系统 ===")

    # 随机生成 10 位评委打分 (范围 60~100 分，符合实际比赛场景)
    scores = [float(random.randint(60, 100)) for _ in range(10)]

    print(f"\n10 个评委的打分为: {[int(s) for s in scores]}")

    results = analyze_competition_scores(scores)

    print(f"最大的分数为: {int(results['max_score'])}")
    print(f"最小的分数为: {int(results['min_score'])}")
    print(f"去掉最高分和最低分，最后得分: {results['avg_score']:.2f}")

    print("\n【评委公正性评定】")
    # 格式化输出最公平评委（支持多位评委并列情况）
    fair_str = ", ".join(
        [f"第 {j_id} 号评委 (打分: {score:g})" for j_id, score in results["most_fair"]]
    )
    print(f"最公平的评委是: {fair_str}")

    # 格式化输出最不公平评委
    unfair_str = ", ".join(
        [f"第 {j_id} 号评委 (打分: {score:g})" for j_id, score in results["most_unfair"]]
    )
    print(f"最不公平的评委是: {unfair_str}")


if __name__ == "__main__":
    main()