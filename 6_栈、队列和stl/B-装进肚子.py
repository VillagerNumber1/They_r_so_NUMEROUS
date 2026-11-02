"""
理解题目: 总共要吃n个巧克力
每天吃n个巧克力, 其中早上吃K个巧克力, 晚上吃n - K个巧克力

对于第二行与第三行,我们看看。
"""
import random
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
if random.randint(1 , 2) == 1: # 保底全吃晚上的
    base_sweetness = 0
    for i in range(0, total_chocolate):
        base_sweetness += int(tonight[i])

    pigeon = []
    for i in range(0 , total_chocolate):
        # 意思是如果挑早上的,我能赚多少?
        difference = int(morning[i]) - int(tonight[i]) # 差值difference
        pigeon.append(difference)

    pigeon.sort(reverse=True) # 大在前, 小在后

    for i in range(0, morning_chocolate):
        base_sweetness += int(pigeon[i])

    print(base_sweetness)

else: # 保底全吃早上的
    base_sweetness = 0
    for i in range(0 , total_chocolate):
        base_sweetness += int(morning[i])

    pigeon = []
    for i in range(0 , total_chocolate):
        # 挑晚上的,我能赚多少?
        difference = -int(morning[i]) + int(tonight[i])
        pigeon.append(difference)

    pigeon.sort(reverse=True)

    for i in range(0 , tonight_chocolate):
        base_sweetness += int(pigeon[i])

    print(base_sweetness)