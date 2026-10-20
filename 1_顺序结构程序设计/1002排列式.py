import time
# 暴力穷举(失败，还是借鉴了别人的做法)

def read_repeat_count(i1,i2,i3):
    i1_str = str(i1)
    i2_str = str(i2)
    i3_str = str(i3)
    
    if '0' in i1_str or '0' in i2_str or '0' in i3_str:
        return 1

    s = i1_str + i2_str + i3_str
    if len(set(s)) == len(s):
        return 0
    else:
        return 1
# 0为没有重复, 1为有重复(或存在0)

def len_check(i1,i2,i3):
    i1_str = str(i1)
    i2_str = str(i2)
    i3_str = str(i3)

    i1_len = len(i1_str)
    i2_len = len(i2_str)
    i3_len = len(i3_str)

    if i1_len + i2_len + i3_len == 9:
        return 1
    else:
        return 0
# 1为长度符合要求, 0为长度不符合要求

i1 = 0
i2 = 0
i3 = 0
result = []

for i2 in range(1,100):
    for i3 in range(i2 + 1 , 9999 // i2 + 1):
        i1 = i2 * i3 
        # 不用验算,因为 i1 = i2 * i3 已经保证了乘法关系
        if i2 < i3 \
        and len_check(i1,i2,i3) == 1 \
        and read_repeat_count(i1,i2,i3) == 0:
            result.append((i1, i2, i3))
            # 列表添加项

result.sort(key=None,reverse=False)  
# 按照 i1 的值进行排序(关键2)

for i1, i2, i3 in result:
    print(f"{i1} = {i2} x {i3}")