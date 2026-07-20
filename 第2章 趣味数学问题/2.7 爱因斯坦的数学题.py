#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc: 爱因斯坦的数学题

def computing_ladder(n: int) -> None:
    # """计算在 1 到 n 之间满足爱因斯坦阶梯要求的数，并打印这些数。

    # 爱因斯坦阶梯问题数学条件：
    # 1. 每次上2阶，剩1阶 => i % 2 == 1 (由 i % 6 == 5 自动蕴含)
    # 2. 每次上3阶，剩2阶 => i % 3 == 2 (由 i % 6 == 5 自动蕴含)
    # 3. 每次上5阶，剩4阶 => i % 5 == 4
    # 4. 每次上6阶，剩5阶 => i % 6 == 5
    # 5. 每次上7阶，刚好走完 => i % 7 == 0

    # Args:
    #     n (int): 查找范围的上限
    # """
    print(f"\n在 1-{n} 之间的阶梯数为：")
    match_count = 0
    
    # 算法优化：由于 i 必须是 7 的倍数，直接将 range 步长设为 7，检索效率提升 7 倍。
    # 此外，若 i % 6 == 5 成立，则 i 必然是奇数（i % 2 == 1）且除以 3 余 2（i % 3 == 2），因此无需重复判断。
    for i in range(7, n + 1, 7):
        if (i % 6 == 5) and (i % 5 == 4):
            match_count += 1
            print(i)
            
    print(f"在 1-{n} 之间，有 {match_count} 个数可以满足爱因斯坦对阶梯的要求。")


if __name__ == "__main__":
    while True:
        try:
            # 增加友好的交互与退出机制
            user_input = input("请输入 n 值（输入 q 退出）：").strip()
            if user_input.lower() == 'q':
                print("程序已成功退出。")
                break
                
            n = int(user_input)
            if n < 7:
                print("提示：阶梯数必须是 7 的正倍数，请输入不小于 7 的整数。")
                continue
                
            computing_ladder(n)
            print("-" * 50)
            
        except ValueError:
            print("输入无效！请输入一个有效的正整数。")
        except (KeyboardInterrupt, EOFError):
            print("\n检测到退出指令，程序已结束。")
            break