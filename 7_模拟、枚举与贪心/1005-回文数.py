"""
马上就好(马上好马上好马上好马上~)
明天能交(明天交明天交明天交明天~)
思路参考: ac.nowcoder.com/acm/contest/view-submission?submissionId=85357064
"""

# 输入部分
import sys
lines = []
for line in sys.stdin.read().split():
    lines.append(int(line))
# ↑注意到数码跟列表的编码是对的上的,有点东西

#(弃用) 判断数码奇odd偶数even
if sum(lines) % 2 == 0:
    odd_or_even = 0
elif sum(lines) % 2 == 1:
    odd_or_even = 1
else:
    exit(114514)

# 奇数次出现次数
odd_count = 0
for i in range(0 , len(lines)):
    if lines[i] % 2 == 1:
        odd_count += 1

# 无解(没想到,超过一个奇数)
if odd_count > 1:
    print(-1)
    exit()

# 特殊情况,只有一个数码
if sum(lines) == 1:
    for i in range(0 , len(lines)):
        if lines[i] == 1:
            print(i)
            exit()

# 特殊情况:全tm是 0
if sum(lines) - lines[0] == 0:
    if lines[0] > 1:
        print(-1)
        exit()

# 特殊情况
# ==========
# 奇数偶数情况一起讨论
temp_list = []
middle = ""

# 找中间数
for i in range(0 , len(lines)):
    if lines[i] % 2 == 1:
        middle = str(i)
        lines[i] -= 1
        break

# 组合左边,右边根据左边推演即可
for i in range(0, len(lines)):
    if lines[i] != 0:
        # 修了只能遍历一次的遗憾
        # 这里除法 // 跟C语言的除法一致
        # 如果都是整型的话,不会四舍五入
        half_count = lines[i] // 2
        for _ in range(half_count):
            temp_list.append(i)

# 处理开头0
# wtf老子找了好久的bug↓ 我giao谁写的1？？？
if len(temp_list) > 0 and temp_list[0] == 0:
    # 既在情理之外,也在意料之中
    found_nonzreo = False
    for i in range(1 , len(temp_list)):
        if temp_list[i] != 0:
            found_nonzreo = True
            temp_list[0], temp_list[i] = temp_list[i], temp_list[0]
            break
    """
    Python可以直接在for后面直接接个else
    即若循环体内未被break,则进入else
    但这样三个双引号注释打出来,会导致代码报错
    所以还是用了通用写法。
    """
    # 如果全是'0'且长度大于1,即无法避免前导 0
    if not found_nonzreo:
        if len(temp_list) * 2 + len(middle) > 1:
            print(-1)
            exit()

# 拼接数字
temp_list_reverse = []
for i_rev in range(-1 , -len(temp_list) - 1 , - 1):
    temp_list_reverse.append(temp_list[i_rev])
temp_list = map(str , temp_list)
temp_list_reverse = map(str , temp_list_reverse)
print("".join(temp_list)+middle+"".join(temp_list_reverse))