#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# @author: CeresBebop
# @desc: 借书方案知多少

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @desc: 借书方案知多少

if __name__ == "__main__":
    # A、B、C三位小朋友，5本书，每人每次只能借一本
    # 用a、b、c分别表示三人所选图书的编号
    i = 0
    print("A,B,C三人所选书号分别为：")
    
    a = 1
    while a <= 5:
        b = 1
        while b <= 5:
            c = 1
            while c <= 5 and a != b:
                if a != c and b != c:
                    # 控制有效借阅组合
                    print("A:%2d  B:%2d  C:%2d    " % (a, b, c), end='')
                    i += 1
                    if i % 4 == 0:
                        print()  # 换行
                c += 1
            b += 1
        a += 1
        
    print("\n共有%d种有效借阅方法" % i)


# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @author : liuhefei
# # @desc: 借书方案知多少

# if __name__ == "__main__":
#     # A、B、C三位小朋友，5本书，每人每次只能借一本
#     # 用a、b、c分别表示三人所选图书的编号
#     i = 0  # i表示有效借阅组合的计数器
#     print("A,B,C三人所选书号分别为：")
    
#     # 使用 for 循环控制每个人选书的范围 1~5
#     for a in range(1, 6):
#         for b in range(1, 6):
#             for c in range(1, 6):
                
#                 # 控制有效借阅组合：三个人选的书不能相同
#                 if (a != b) and (a != c) and (b != c):
#                     print("A:%2d  B:%2d  C:%2d    " % (a, b, c), end='')
#                     i += 1
                    
#                     # 每打印 4 个组合就换一行
#                     if i % 4 == 0:
#                         print()
                        
#     print("\n共有%d种有效借阅方法" % i)