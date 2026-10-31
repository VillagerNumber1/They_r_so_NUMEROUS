import sys
"""
这道题目还挺经典的，金字塔题目。
"""

data = sys.stdin.read().split()
if data: # 审题:第一组数字T
    T = int(data[0])
    n_list = []
    for i in range(1, T + 1):
        n_list.append(int(data[i]))
# 输入部分我真没招了,对待刷题这类问题,
# 确实不应该加入try去判定错谬与否。


def space(space_count):
    for i in range(1 , int(space_count / 2) + 1):
        print(end=" ")

def star(star_count):
    for i in range(1 , star_count + 1):
        print(end="*")
    print(end="\n")


n = sorted(list(set(n_list)),reverse=False)
# 集合是无序的,所以先利用集合剔除重复元素的特点，、
# 再换回列表并排序，接下来就如法炮制了。

for n1 in n:
    # 数据处理部分
    reverse = 0
    star_count = 1
    n1 = int(n1)
    backup_n1 = n1

    # 特殊情况处理
    if n1 == 1:
        print("*",end="\n")
        continue

    while True:
        # 上下部分
        if reverse == 0 and int(n1 / 2) >= 0:
            space(n1)
            star(star_count)
            n1 -= 2
            star_count += 2
        elif reverse == 1 and int(n1 / 2) >= 0:
            space(n1)
            star(star_count)
            n1 += 2
            star_count -= 2

        # 后台处理
        if reverse == 0 and int(n1 / 2) == 0:
            reverse = 1
            star(star_count)
            n1 += 2
            star_count -= 2
        if reverse == 1 and backup_n1 < n1:
            break