# 注释:素数,即质数。
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数。

t = input()
t_back_count = t

# 1增2减~先弄个初始值
if int(t[0]) - int(t[1]) < 0:
    up_1_down_2 = 1
elif int(t[0]) - int(t[1]) > 0:
    up_1_down_2 = 2
else:
    print("noprime") # 狗运(一开始就不是素数,极其难绷)
    exit()

# 原先的t是否为素数
for qwq in range(1 , len(t)-1):
    if int(t[qwq]) - int(t[qwq+1]) < 0 and up_1_down_2 == 2:
        print("noprime")
        exit()
    elif int(t[qwq]) - int(t[qwq+1]) > 0 and up_1_down_2 == 1:
        print("noprime")
        exit()
    elif int(t[qwq]) - int(t[qwq+1]) == 0:
        print("noprime")
        exit()

# 先处理成回文数t_back_count
if len(t) % 2 == 0:
    for i in range(-1 , -len(t) - 1 , -1):
        t_back_count = t_back_count + t[i]
elif len(t) % 2 == 1:
    for i in range(-1 , -len(t) , -1):
        t_back_count = t_back_count + t[i]

# 检验回文数是否为素数
for awa in range(1 , len(t_back_count)-1):
    if int(t[awa]) - int(t[awa+1]) < 0 and up_1_down_2 == 2:
        print("noprime")
        exit()
    elif int(t[awa]) - int(t[awa+1]) > 0 and up_1_down_2 == 1:
        print("noprime")
        exit()
    elif int(t[awa]) - int(t[awa+1]) == 0:
        print("noprime")
        exit()