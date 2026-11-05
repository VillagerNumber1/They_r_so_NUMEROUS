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

# 判断数码奇odd偶数even
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

# 无解(没想到)
if odd_count > 1:
    print(-1)
    exit()

# 特殊情况,只有一个数码
if sum(lines) == 1:
    for i in range(0 , len(lines)):
        if lines[i] == 1:
            print(i)
            exit()

"""屎山的出现"""
# # 特殊情况:0 被迫放前面
# if lines[0] >= sum(lines) - lines[0]:
#     print(-1)
#     exit()

# 数码为 奇(1)odd 和 偶(0)even 的情况：
# ==========

# 偶数情况
if odd_or_even == 0:
    temp_list = []
    # 开头先找 1
    for i in range(1 , len(lines)):
        if lines[i] != 0:
            temp_list.append(i)
            lines[i] -= 1
            break
    # 然后从0开始查找
    for i in range(0 , len(lines)):
        if lines[i] != 0 and lines[i] % 2 == 0:
            temp_list.append(i)
            # 修了了只能遍历一次的遗憾
            # Tips: / 浮点数 ; // 取整
            half_count = int(lines[i] / 2) - 1
            if half_count > 0:
                for _ in range(half_count):
                    temp_list.append(i)
    # 找完了,拼接数字
    """
    为什么直接按照原来列表反接呢？
    因为前面已经排除了奇数的情况。
    所以偶数这里就偷懒啦~
    (跟那群大哥写 for qwq in range(10)是差不多的)
    """
    temp_list_reverse = []
    for i_rev in range(-1 , -len(temp_list) - 1 , - 1):
        temp_list_reverse.append(temp_list[i_rev])
    # 拼接输出
    temp_list = map(str , temp_list)
    temp_list_reverse = map(str , temp_list_reverse)
    print("".join(temp_list)+"".join(temp_list_reverse))

# ==========
# 奇数情况
elif odd_or_even == 1:
    middle = []
    temp_list = []
    for i in range(0 , len(lines)):
        # 我先找下奇数的数码位置
        if lines[i] % 2 == 1:
            middle.append(i)
            lines[i] -= 1
            break
    # 然后就是跟上面一样,如法炮制。先找1。
    for i in range(1 , len(lines)):
        if lines[i] != 0:
            temp_list.append(i)
            lines[i] -= 1
            break
    # 然后从0开始查找
    for i in range(0 , len(lines)):
        if lines[i] != 0 and lines[i] % 2 == 0:
            temp_list.append(i)
            # 修了了只能遍历一次的遗憾
            half_count = int(lines[i] / 2) - 1
            if half_count > 0:
                for _ in range(half_count):
                    temp_list.append(i)
    # 中间数插入
    temp_list.append(middle[0])
    # 找完了,拼接数字(跳过中间数)
    temp_list_reverse = []
    for i_rev in range(-2 , -len(temp_list) - 1 , - 1):
        temp_list_reverse.append(temp_list[i_rev])
    # 拼接输出
    temp_list = map(str , temp_list)
    temp_list_reverse = map(str , temp_list_reverse)
    print("".join(temp_list)+"".join(temp_list_reverse))