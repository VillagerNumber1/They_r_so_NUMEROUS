import sys

# 按行读取
data = sys.stdin.read().split()
if data == '':
    exit()

# 第一行: L马路长度;M地铁施工区域数

basic_data = data[0]
"""
易错: 未处理成int拿到的是字符串,结果得到的是5
"""
L = int(data[0])
M = int(data[1])

# 接下来便是遍历(注意题目要求闭区间)
tree_tag = []
"""
拓扑图草稿

tree_tag → row → 区间整数遍历 * 114514
"""
tree_remove = 0
tree_remove_distinct = 0
for row in range(1 , int(basic_data[1]) + 1):
    # iloveyou = 0 # 我崩溃了,反正是专用于list的编号()
    for tree_count in range(int(data[row][0]) , int(data[row][1]) + 1):
        tree_tag[row][tree_count] = tree_count # 给集合作铺垫,我没记错的话
        tree_remove += int(data[row][1]) + 1 - int(data[row][0])

# 遍历是否有重复
for i in range(1 , int(basic_data[1]) + 1):
    for j in range(1 , int(basic_data[1]) + 1):
        if i < j:
             set1 = set()
             set1.add(tree_tag[i])
             set1.add(tree_tag[j])
             tree_remove_distinct += len(set1)

tree_actually = int(basic_data[0]) - tree_remove + tree_remove_distinct
print(f"{tree_actually}")