import time
# 暴力穷举

def read_repeat_count(i1,i2,i3):
    i1_str = str(i1)
    i2_str = str(i2)
    i3_str = str(i3)

    s = i1_str + i2_str + i3_str
    if len(set(s)) == len(s):
        return 0
    else:
        return 1

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

i1 = 0
i2 = 0
i3 = 0
for i1 in range(1000,9999):
    for i2 in range(1,1000):
        for i3 in range(1,1000):
            if i2 < i3 \
            and len_check(i1,i2,i3) == 1 \
            and read_repeat_count(i1,i2,i3) == 0 \
            and i1 == i2 * i3:
                print(i1,"=",i2,"*",i3)
            else:
                continue