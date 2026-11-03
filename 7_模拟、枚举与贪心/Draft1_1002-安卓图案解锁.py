import sys
total = sys.stdin.read().split()

# 测是否跳过数字了(传入列表内数字)
def jump_num(a , b):
    all_possible = [1,3,7,9]
    if a in all_possible and b in all_possible:
        return True
    elif a == b: # 有相同的数字可以直接排除了
        print("NO")
        exit()
    else:
        return False

# 跳过数字可能的范围
def jump_range(now_num):
    number_1 = [4,5,2]
    number_3 = [2,5,6]
    number_7 = [4,5,8]
    number_9 = [8,5,6]
    if now_num == 1:
        return number_1
    elif now_num == 3:
        return number_3
    elif now_num == 7:
        return number_7
    elif now_num == 9:
        return number_9

# 本想着数学方法解决,结果发现似乎不需要def函数
def jump_range_v2(now_num):
    man_what_can_i_say = 0
    return 114514

# 这个读取部分我不知道咋写,一开始当作单组输入了,完犊子。
for line in total:
    reading = line
reading = sys.stdin
reading = list(reading)

# 如果有重复的数字,那肯定是NO
for i in range(0 , len(reading)):
    for j in range(i + 1 , len(reading)):
        if reading[i] == reading[j]:
            print("NO")
            exit()
del i,j

# 总处理部分
bro_what_happen = 0
for mainloop in range(0 , len(reading) - 1):
    if jump_num(reading[mainloop] , reading[mainloop + 1]) == True:
        target_num = int(reading[mainloop]) + int(reading[mainloop + 1]) / 2

        for backback in range(int(reading[mainloop]) , -1 , -1):
            if reading[backback] == target_num:
                bro_what_happen = 0
                break
            else:
                bro_what_happen += 1

        if bro_what_happen > 0:
            print("NO")
            exit()
print("YES")