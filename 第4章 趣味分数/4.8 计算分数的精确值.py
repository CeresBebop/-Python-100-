#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc   : 计算分数的精确值（精确长除法与循环节分析）


def calculate_exact_fraction(m: int, n: int) -> dict[str, object]:
    """计算分数 m/n 的精确小数形式，自动提取有限小数或无限循环小数的循环节。

    算法原理：
    模仿长除法（手动除法）过程，利用哈希表记录余数的历史出现位置：
    1. 每次求商并计算余数 m。
    2. 若余数 m == 0，说明是有限小数，计算完成。
    3. 若余数 m 在之前已经出现过（记起始位置为 start_pos），说明进入了小数循环，
       从 start_pos 到当前位置的商即为【循环节】。

    Args:
        m (int): 分子 (正整数)
        n (int): 分母 (正整数)

    Returns:
        dict[str, object]: 包含精确计算结果、循环节内容、起始位置和长度的字典

    Raises:
        ValueError: 当分母为 0 或分子分母非正数时抛出
    """
    if n <= 0 or m <= 0:
        raise ValueError("分子和分母必须均为大于 0 的正整数")

    integer_part = m // n
    remainder_val = m % n

    # 若余数为 0，说明结果为整数
    if remainder_val == 0:
        return {
            "is_repeating": False,
            "exact_str": str(integer_part),
            "integer_part": integer_part,
            "repeat_cycle": "",
            "start_pos": None,
            "cycle_length": 0,
        }

    remainder_pos = {}  # 记录 余数 -> 在小数部分的第几位出现 (从 1 开始)
    quotients = []      # 依次记录小数部分的每一位商
    pos = 1

    curr_rem = remainder_val

    while curr_rem != 0:
        # 判断当前余数是否曾经出现过
        if curr_rem in remainder_pos:
            start_pos = remainder_pos[curr_rem]
            # 截取非循环部分与循环节数字串
            non_repeat_digits = "".join(map(str, quotients[: start_pos - 1]))
            repeat_digits = "".join(map(str, quotients[start_pos - 1 :]))

            exact_formatted = (
                f"{integer_part}.{non_repeat_digits}({repeat_digits})"
            )

            return {
                "is_repeating": True,
                "exact_str": exact_formatted,
                "integer_part": integer_part,
                "repeat_cycle": repeat_digits,
                "start_pos": start_pos,
                "cycle_length": len(repeat_digits),
            }

        # 记录当前余数第一次出现的位数位置 pos
        remainder_pos[curr_rem] = pos

        # 模拟长除法：余数扩大 10 倍求商和余数
        curr_rem *= 10
        q_digit = curr_rem // n
        curr_rem %= n

        quotients.append(q_digit)
        pos += 1

    # 余数降为 0，说明是有限小数
    decimal_digits = "".join(map(str, quotients))
    return {
        "is_repeating": False,
        "exact_str": f"{integer_part}.{decimal_digits}",
        "integer_part": integer_part,
        "repeat_cycle": "",
        "start_pos": None,
        "cycle_length": 0,
    }


def main() -> None:
    """主程序入口，支持交互输入与零配置默认回退逻辑。"""
    print("=== 分数精确值与循环节分析程序 ===")

    # 零配置容错：直接按回车默认使用经典测试用例 m = 1, n = 7
    raw_input = input("请输入分子 m 和分母 n (空格分隔) [直接回车默认 1 7]: ").strip()

    if not raw_input:
        m, n = 1, 7
        print(f"未检测到输入，自动加载默认测试用例: {m}/{n}")
    else:
        try:
            parts = raw_input.split()
            if len(parts) != 2:
                raise ValueError("必须输入由空格分隔的两个正整数")
            m, n = int(parts[0]), int(parts[1])
        except ValueError as err:
            print(f"输入格式解析失败 ({err})，自动加载默认测试用例: 1/7")
            m, n = 1, 7

    print(f"输入的分数为: {m}/{n}")

    try:
        res = calculate_exact_fraction(m, n)
        print(f"\n{m}/{n} 的精确表达式: {res['exact_str']}")

        if res["is_repeating"]:
            print("【小数类型】: 无限循环小数")
            print(f"【第一个循环节数字】: {res['repeat_cycle']}")
            print(f"【循环节起始位置】: 小数点后第 {res['start_pos']} 位")
            print(f"【循环节长度】: {res['cycle_length']} 位")
        else:
            print("【小数类型】: 有限小数")

    except ValueError as e:
        print(f"计算失败: {e}")


if __name__ == "__main__":
    main()