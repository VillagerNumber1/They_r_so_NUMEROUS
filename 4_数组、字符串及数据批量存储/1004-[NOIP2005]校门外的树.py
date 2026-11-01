import random
calculate_way = random.randint(1,2)

# 按行读取
L,M = map(int,input().split()) # 受不鸟了,stdin好反人类啊。

"""
思路: 把每棵树编号,装进road列表里。
"""
road = []
for i in range(L + 1):
    road.append(1)

# 循环M次,每次读一行施工区域
for ILoveYou in range(M):
    l,r = map(int,input().split())
    for i in range(l , r + 1):
        road[i] = 0
        # 喵的个这个方法怎么这么聪明啊！！！

# 列表里的树都是1,太妙了这个方法！！！
# 甚至可以for循环列表所有元素,然后输出
if calculate_way == 1:
    print(sum(road))
elif calculate_way == 2:
    num_total = 0
    for i in range(0 , len(road)):
        num_total += road[i]
    print(num_total)

# 原来如此,高中数学陷害我。
# 呜呜呜呜呜呜呜呜呜呜。

"""
如果使用idx索引的话
或许会更好一点...(主要我不会=-=)
"""