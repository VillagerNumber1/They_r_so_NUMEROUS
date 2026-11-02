"""
理解题目: 总共要吃n个巧克力
每天吃n个巧克力, 其中早上吃K个巧克力, 晚上吃n - K个巧克力

对于第二行与第三行,我们看看。
"""
import sys
lines = []
for line in sys.stdin.read().split():
    lines.append(line)

# 第一行信息
total_chocolate = int(lines[0])
morning_chocolate = int(lines[1])
tonight_chocolate = total_chocolate - morning_chocolate

# 第二行信息,第三行信息
morning = []
for two_row in range(2 , 2 + total_chocolate):
    morning.append(int(lines[two_row]))
tonight = []
for three_row in range(2 + total_chocolate , 2 + 2*total_chocolate):
    tonight.append(int(lines[three_row]))

# 根据场外援助,我们使用贪心法,目光短浅法
pigeon = []
for i in range(0 , total_chocolate):
    if int(morning[i]) < int(tonight[i]):
        pigeon.append(int(tonight[i]))
    elif int(morning[i]) > int(tonight[i]):
        pigeon.append(int(morning[i]))
    else:
        pigeon.append(int(morning[i]))
print(sum(pigeon))