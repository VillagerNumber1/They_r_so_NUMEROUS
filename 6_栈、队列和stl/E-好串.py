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
    for i in range(0 , len(chuanchuan_temp) - 1): # 修复了可能越界的bug
        if (chuanchuan_temp[i] + chuanchuan_temp[i+1]) == 'ab':
            del chuanchuan_temp[i]
            del chuanchuan_temp[i]
            # md怎么这么难绷,列表好像是动态变化的
            break
        else:
            if ('a' in chuanchuan_temp and 'b' not in chuanchuan_temp) or \
            ('b' in chuanchuan_temp and 'a' not in chuanchuan_temp):
                print("Bad")
                exit()
            elif ('ab' not in "".join(chuanchuan_temp)) and \
            ('ba' in "".join(chuanchuan_temp)):
                print("Bad")
                exit()


    if not chuanchuan_temp: # 如果删没了
        print("Good")
        exit()

    