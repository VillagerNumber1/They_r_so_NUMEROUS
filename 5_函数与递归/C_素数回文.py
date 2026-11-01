# 注释:素数,即质数。
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数。

t = input()
t_back_count = t

"""
个人认为,语文对理解题意至关重要。
虽然提升语文一事使我本来就差的语文雪上加霜。
"""

# 先转换成回文数
if len(t) == 1: # 特殊情况
    t_back_count = t_back_count * 2
elif len(t) % 2 == 0: # 偶数项
    for qwq in range(-2, -len(t)-1 , -1):
        t_back_count += t[qwq]
        # print(t_back_count)
elif len(t) % 2 == 1: #奇数项
    for awa in range(-2, -len(t)-1 , -1):
        t_back_count += t[awa]
        # print(t_back_count)


# 判断这个回文数是否为素数
import math

t_back_count = t_back_count.replace("-","") # python你别乱加东西好么qwq
t_back_count = int(t_back_count)
t_back_count_sqrt = int(math.sqrt(t_back_count))

if t_back_count < 2:
    print("noprime")
    exit()
for calculate in range(2 , t_back_count_sqrt + 1):
    if t_back_count % calculate == 0: 
        print("noprime")
        exit()
print("prime")