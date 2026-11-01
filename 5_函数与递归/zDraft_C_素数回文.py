# 注释:素数,即质数。
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数。

t = input()
# 1增2减~先弄个初始值
if int(t[0]) - int(t[1]) < 0:
    up_1_down_2 = 1
elif int(t[0]) - int(t[1]) > 0:
    up_1_down_2 = 2
for n in range(0 , len(t)):
    if int(t[n]) - int(t[n+1]) != up_1_down_2:
        print("noprime")
