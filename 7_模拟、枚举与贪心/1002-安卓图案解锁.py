# 字典查表
dictionary = {
    (1, 3): 2, (3, 1): 2,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8,
    (1, 7): 4, (7, 1): 4,
    (2, 8): 5, (8, 2): 5,
    (3, 9): 6, (9, 3): 6,
    (1, 9): 5, (9, 1): 5,
    (3, 7): 5, (7, 3): 5,
}

# 输入部分
import sys
import random
random_select = random.randint(1 , 2)
lines = []
for line in sys.stdin.read().split():
    lines.append(line)
del line

# 处理部分
for group in range(0, len(lines)):
    # 读出每组数字
    reading = lines[group]
    reading = list(reading)

    # 检查是否有重复数字(两种方法混合双打)
    if random_select == 1: # 法一: 集合法
        reading_set = set(reading)
        if len(reading) != len(reading_set):
            print("NO")
            del reading_set
            continue
        else:
            del reading_set
    elif random_select == 2: # 法二: 循环查重法(略麻烦)
        break_code = 0
        for i in range(0 , len(reading)):
            for j in range(0 , len(reading)):
                if i == j:
                    continue
                elif reading[i] == reading[j]:
                    print("NO")
                    break_code = 1
                    break
            if break_code == 1:
                break
        if break_code == 1:
            break_code = 0 # 变量复用
            continue
    
    # 对当前组数字进行读取
    visited = set()
    for i in range(0 , len(reading) - 1):
        a = int(reading[i])
        b = int(reading[i + 1])

        # 列表、集合均可,主要目的是检查是否经过中间点了
        visited.add(a)

        # 重头戏--查字典
        if (a, b) in dictionary:
            middile_point = dictionary[(a, b)]
            if middile_point not in visited:
                print("NO")
                break_code = 1
                break

    # 防止连环"NO"+"YES"
    if break_code == 1:
        continue
    print("YES")