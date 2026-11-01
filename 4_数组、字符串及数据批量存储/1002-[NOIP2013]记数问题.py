import sys

data = sys.stdin.read().split()

# 上界
upper_n = int(data[0])
# 数字
number_x = str(data[1])
# 出现次数
appear_number = 0

for now_num in range(1 , upper_n + 1):
    now_num = str(now_num)
    for i in range(len(now_num)):
        """
        反思:python里的类型转化对CPU性能开销极大
        对于算法题而言这是很致命的。
        AI 推荐用count()或者O(logN)
        """
        if now_num[i] == number_x:
            appear_number += 1
print(appear_number)