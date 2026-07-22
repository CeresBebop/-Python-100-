#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 互质勾股数 (Coprime Pythagorean Triples Generator)

def generate_coprime_pythagorean_triple(a: int) -> tuple[int, int, int]:
    """根据指定的 a 值，利用特定的代数公式生成互质的勾股数。

    算法原理：
    1. 当 a 为大于等于 3 的奇数时 (a = 2n + 1):
       令 n = (a - 1) // 2，则 b = 2*n^2 + 2*n，c = 2*n^2 + 2*n + 1。
       此时 c - b = 1，相邻两数天然互质，进而保证三元组绝对互质。
    2. 当 a 为大于等于 4 且能被 4 整除的偶数时 (a = 2n，且 n 为偶数):
       令 n = a // 2，则 b = n^2 - 1，c = n^2 + 1。
       此时 b、c 为两个连续的奇数，差为 2，因而必互质，同样保证三元组互质。
       注意：普通偶数（如 6）因无法保证结果互质而被本算法严格拦截。

    Args:
        a (int): 给定的直角边 a。

    Returns:
        tuple[int, int, int]: 满足 a^2 + b^2 = c^2 且 gcd(a, b, c) == 1 的三元组。

    Raises:
        ValueError: 当输入的 a 无法生成符合互质条件的勾股数时抛出。
    """
    # 情况一：a 为大于等于 3 的奇数
    if a >= 3 and a % 2 == 1:
        n = (a - 1) // 2
        b = 2 * n**2 + 2 * n
        c = 2 * n**2 + 2 * n + 1
        return a, b, c

    # 情况二：a 为能被 4 整除的偶数（严格拦截 6 等不互质的偶数）
    elif a >= 4 and a % 4 == 0:
        n = a // 2
        b = n**2 - 1
        c = n**2 + 1
        return a, b, c

    # 其他不满足互质勾股数公式要求的情况
    else:
        raise ValueError(
            f"数值 {a} 无法通过经典公式生成互质勾股数。\n"
            f"数学要求：a 必须是 >= 3 的奇数，或 >= 4 且能被 4 整除的偶数。"
        )


def main() -> None:
    """主入口函数。安全获取用户输入并计算打印互质勾股数。"""
    try:
        user_input = input("请输入直角边 a 的值（回车默认 15）：").strip()
        # 兼容空输入回车，提供默认测试数据以实现免配置一键运行
        a = int(user_input) if user_input else 15

        # 调用核心算法生成三元组
        a_val, b_val, c_val = generate_coprime_pythagorean_triple(a)
        
        print(f"\n生成成功！互质勾股数为:")
        print(f"a = {a_val}, b = {b_val}, c = {c_val}")
        print(f"验证等式: {a_val}^2 + {b_val}^2 = {c_val}^2  ->  {a_val**2} + {b_val**2} = {c_val**2}")

    except ValueError as e:
        # 捕获非法输入和不合规的数据范围，友好提示
        print(f"\n[运行失败] {e}")


if __name__ == '__main__':
    main()