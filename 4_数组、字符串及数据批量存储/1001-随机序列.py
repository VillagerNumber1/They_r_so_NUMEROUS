import sys

T = list(sys.stdin.read().split("\n"))

test_paper_count = int(T[0])

for i in range(1, test_paper_count + 1):
    # 读取数字总共的数量
    number_count = T[2*i - 1] # 有个范围的,懒得写判断了。1<=n<=10**5
    number_count = int(number_count)

    # 读取指定行的数字
    a = list(int(x) for x in T[2*i].split())
    """
    坑: 需要事先把列表内字符串读成数字(本题为整数),
    否则后续计算会出错。卧槽跟箭形图案一样坑爹。

    或者直接用max()和min()算极差。
    不过还是排序更符合直觉。
    """
    a = sorted(a, reverse=False)
    a_total = 0
    a_variance = 0

    # 计算极差、平均值、方差
    exterme_difference = int(a[-1]) - int(a[0]) # 极差
    for qwq in range(0, number_count):
        a_total += int(a[qwq]) # a的总数
    a_average = a_total / number_count # 平均值
    for qwq in range(0, number_count):
        a_variance += (int(a[qwq]) - a_average) ** 2 # 方差(先算总数)
    a_variance = a_variance / number_count # 方差(再除以总数)

    # 输出
    print(f"{int(exterme_difference)} {a_variance:.3f}")