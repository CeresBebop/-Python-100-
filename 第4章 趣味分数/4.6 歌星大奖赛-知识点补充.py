#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : Python random 模块常用随机数/序列操作函数用法示例与修正


def demonstrate_random_functions() -> dict[str, object]:
    """演示 Python 内置 random 模块各种常用随机数生成与序列操作函数的用法。

    函数说明与区别：
    - random.random(): 生成 [0.0, 1.0) 之间的随机浮点数。
    - random.randint(a, b): 生成 [a, b] 双闭区间的随机整数（包含 a 和 b）。
    - random.randrange(start, stop[, step]): 生成 [start, stop) 左闭右开区间的随机整数。
    - random.uniform(a, b): 生成 [a, b] 之间的随机浮点数。
    - random.choice(seq): 从非空序列 seq 中随机抽取 1 个元素。
    - random.sample(population, k): 从总体中随机无放回抽取 k 个不重复元素。
    - random.shuffle(x): 原地打乱可变序列 x 的元素顺序。

    Returns:
        dict[str, object]: 包含各随机操作生成结果的字典
    """
    import random

    results = {}

    # 1. 生成 [0.0, 1.0) 之间的随机小数
    a = random.random()
    results["a"] = a
    print(f"a = {a}  (0 到 1 之间的随机小数)")

    # 2. 生成 [0, 101) 半开区间之间的随机整数
    # 注意：原代码使用 randint(0, 101) 为闭区间 [0, 101]；若要表达 [0, 101) 建议使用 randrange(0, 101)
    b = random.randrange(0, 101)
    results["b"] = b
    print(f"b = {b}  ([0, 101) 半开区间内的随机整数)")

    # 3. 生成 [0, 10) 之间的随机小数
    c = random.uniform(0, 10)
    results["c"] = c
    print(f"c = {c}  ([0, 10) 之间的随机小数)")

    # 4. 随机生成 [0, 101) 之间的偶数（步长为 2）
    d = random.randrange(0, 101, 2)
    results["d"] = d
    print(f"d = {d}  ([0, 101) 之间的随机偶数)")

    # 5. 从指定字符串中随机抽取一个字符
    e = random.choice("abcdefg&#%^*f")
    results["e"] = e
    print(f"e = '{e}'  (从字符集合中随机选取的字符)")

    # 6. 从字符串/列表中随机选择一个元素
    fruits = ["apple", "pear", "peach", "orange", "banana"]
    f = random.choice(fruits)
    results["f"] = f
    print(f"f = '{f}'  (从水果列表中随机选取的元素)")

    # 7. 从 26 个英文字母中随机抽取 3 个不重复字符
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    g = random.sample(alphabet, 3)
    results["g"] = g
    print(f"g = {g}  (无放回随机抽取的 3 个字符)")

    # 8. 将列表元素随机打乱（原地洗牌算法）
    num = [9, 6, 4, 0, 2, 5, 3, 7, 1, 8]
    num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    random.shuffle(num)
    results["num"] = num
    print(f"num = {num}  (打乱顺序后的 num 列表)")

    random.shuffle(num1)
    results["num1"] = num1
    print(f"num1 = {num1}  (打乱顺序后的 num1 列表)")

    return results


def main() -> None:
    """主程序入口。"""
    print("=== Python random 模块功能演示 ===")
    demonstrate_random_functions()


if __name__ == "__main__":
    main()