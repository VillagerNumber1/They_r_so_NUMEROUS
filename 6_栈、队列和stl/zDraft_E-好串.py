chuanchuan = input().strip() # 串串
chuanchuan = list(chuanchuan)
# print(chuanchuan)

# 这个方法只能排除一部分,反向的没办法。
statistic_a = 0
statistic_b = 0
for stringqwq in chuanchuan:
    if stringqwq == 'a':
        statistic_a += 1
    elif stringqwq == 'b':
        statistic_b += 1
del stringqwq
if statistic_a != statistic_b:
    print("Bad")
    exit()

# 哦,我想到了个奇妙的办法,真是气人。
chuanchuan_temp = chuanchuan
try_count = 0
i = 0
while True:
    # list index out of range
    if len(chuanchuan_temp) + 1 <= i and try_count >= 4:
        print("Bad")
        exit()
    elif len(chuanchuan_temp) + 1 <= i:
        i = 0
        try_count += 1
        continue

    # 列表遍历
    if str(chuanchuan_temp[i] + chuanchuan_temp[i+1]) == 'ab':
        del chuanchuan_temp[i]
        del chuanchuan_temp[i + 1]
        i = 0
        continue

    i += 1

    if not chuanchuan_temp: # 如果删没了
        print("Good")
        exit()

    