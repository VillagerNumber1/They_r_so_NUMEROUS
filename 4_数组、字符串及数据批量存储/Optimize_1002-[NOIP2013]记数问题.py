import sys

data = sys.stdin.read().split()
if not data:
    exit()

# 上界
upper_n = int(data[0])
# 数字(先转换成字符串)
number_x = str(data[1])
# 出现次数
appear_number = 0

for now_num in range(1 , upper_n + 1):
    now_num = str(now_num)
    # 由于下面这行代码使用接近C语言底层,所以会更快
    appear_number += str(now_num).count(number_x)

print(appear_number)