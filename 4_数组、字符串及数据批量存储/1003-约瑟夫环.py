import sys

data = sys.stdin.read().split()

# 玩家编号排序
person_num = int(data[0])
uid = []
for i in range(0,person_num):
    uid.append(i) # 可能有更好的办法

# 从编号为k的人开始报数
uid_select = int(data[1])
# 报数步进
move = int(data[2])
backup_move = move

now_select = uid_select
while True:
    # 大王的出现
    if len(uid) == 1:
        print(uid[0])
        break

    # 修了一个bug
    if uid_select > len(uid) - 1:
        uid_select = 0

    # 什么原地跳一下再前进
    while move > 1:
        uid_select += 1
        move -= 1
        if uid_select > len(uid) - 1:
            uid_select = 0

    move = backup_move # 恢复原来的步进次数(虽然好像可以用for)

    if len(uid) > 1:
        # print(f"元素{uid}")
        del uid[uid_select]
        # print(f"选取元素{uid_select}")