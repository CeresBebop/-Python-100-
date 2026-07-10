#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : CeresBebop
# @desc : 个人所得税问题（阶梯税率计算）

# 个税起征点（收入超过 2000 的部分才需要纳税）
TAXBASE = 2000

# 税率表 TaxTable 是一个列表，包含 9 个元组。
# 每个元组的格式为: (该阶段起点, 该阶段截止点, 该阶段税率)
# 注意：原代码注释中将税率误写为第三个值，但在元组里索引是 2（即第3个元素）
TaxTable = [
    (0, 500, 0.05),
    (500, 2000, 0.10),
    (2000, 5000, 0.15),
    (5000, 20000, 0.20),
    (20000, 40000, 0.25),
    (40000, 60000, 0.30),
    (60000, 80000, 0.35),
    (80000, 100000, 0.40),
    (100000, 1e10, 0.45) # 1e10 表示一个极大的数（100亿），代表 10 万以上无限大
]

# 计算税收的函数
def CalculateTax(profit):
    tax = 0.0  # 初始化总税额为 0.0
    
    # 计算需要纳税的应纳税所得额（总收入减去起征点）
    # 例如：输入 5678，减去 2000 后，应纳税所得额 profit 为 3678
    profit -= TAXBASE 
    
    # 如果收入低于起征点，直接返回 0
    if profit <= 0:
        print("未达到个税起征点，无需缴税。")
        return 0.0

    # 遍历税率表，逐级计算每一段的税额
    for i in range(len(TaxTable)):
        # 获取当前税率档次的 起点、终点、税率
        start = TaxTable[i][0]
        end = TaxTable[i][1]
        rate = TaxTable[i][2]
        
        # 判断当前的应纳税所得额是否超过了当前档次的起点
        if profit > start:
            # 情况 A：应纳税所得额超过了当前档次的上限
            if profit > end:
                # 这一档直接“扣满”，这一段的应纳税金额为 (上限 - 下限)
                current_tax = (end - start) * rate
                tax += current_tax
                
                # 打印当前档次的缴税详情
                print("征税范围: %6d~%6d  该范围内缴税金额: %6.2f  超出该范围的金额: %6d" % 
                      (start, end, current_tax, profit - end))
            
            # 情况 B：应纳税所得额处于当前档次之间（未超过当前上限）
            else:
                # 这一档只扣除超出起点到自身金额的部分：(当前金额 - 下限)
                current_tax = (profit - start) * rate
                tax += current_tax
                
                print("征税范围: %6d~%6d  该范围内缴税金额: %6.2f  超出该范围的金额: %6d" % 
                      (start, end, current_tax, 0))
                
                # 已经计算到了应纳税额的尽头，后续更高的税率档次无需再遍历，直接结束循环
                break
                
    return tax

if __name__ == '__main__':
    print("请输入个人收入金额: ", end='')
    
    try:
        profit = int(input()) # 接收用户输入的总收入
        # 调用函数计算税额
        tax = CalculateTax(profit) 
        print("您的个人所得税为: %12.2f" % tax)
    except ValueError:
        print("请输入合法的数字！")