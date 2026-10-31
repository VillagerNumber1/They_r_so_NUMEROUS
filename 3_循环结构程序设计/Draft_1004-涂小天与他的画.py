import sys
"""
这道题目还挺经典的，金字塔题目。
"""
def space(space_count):
    for i in range(1 , int(space_count / 2) + 1):
        print(end=" ")

def star(star_count):
    for i in range(1 , star_count + 1):
        print(end="*")
    print(end="\n")

# 输入部分
n_list = []

# 遍历所有输入的行
for line in sys.stdin:
    line = line.strip()
    if not line: # 为空时,返回False,判空写法很聪明
        continue
    
    # 提取数字
    parts = line.strip()
    for number in parts:
        try:
            num = int(number)
            # 验证：正整数，奇数，且在 1~49 之间
            if num % 2 == 1 and 1 <= num <= 49:
                n_list.append(num)
            else:
                print("似乎有不对劲的数据~请重新输入。")
        except ValueError:
            print(f"不对劲：{number} 不是纯数字！")

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