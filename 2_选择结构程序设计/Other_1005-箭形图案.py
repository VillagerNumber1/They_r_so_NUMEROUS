import sys
 
for a in sys.stdin:              # a 就是这一行的输入（一行一行读，读完自动结束）
    if a.strip() == '':          # 空行跳过
        continue
 
    n = int(a) + 1               # 题目的箭一共 n+1 层，每层星号多 1 个、空格少 2 个
 
    # 上半部分：1 个星 ... n 个星
    for i in range(1, n + 1):
        b = ' ' * (2 * (n - i))  # b 是这一行前面的空格（每次少 2 个）
        c = '*' * i              # c 是这一行的星号（每次多 1 个）
        print(b + c)
 
    # 下半部分：n-1 个星 ... 1 个星
    for i in range(n - 1, 0, -1):
        b = ' ' * (2 * (n - i))
        c = '*' * i
        print(b + c)