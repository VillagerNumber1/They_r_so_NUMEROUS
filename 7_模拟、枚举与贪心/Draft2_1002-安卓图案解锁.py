# 测是否跳过数字了(传入列表内数字)
def jump_num(a , b):
    a = int(a)
    b = int(b)
    all_possible = [1,3,7,9]
    if a in all_possible and b in all_possible:
        return True
    else:
        return False

#[弃用] 跳过数字可能的范围
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

#[弃用] 本想着数学方法解决,结果发现似乎不需要def函数
def jump_range_v2(now_num):
    man_what_can_i_say = 0
    return 114514

# 总处理部分
def process_part():
    # 1、重复数字处理
    for i in range(0 , len(reading)):
        for j in range(0 , len(reading)):
            if i == j:
                continue
            elif reading[i] == reading[j]:
                print("NO")
                return -1
    del i,j

    bro_what_happen = 0
    for mainloop in range(0 , len(reading) - 1):
        if jump_num(reading[mainloop] , reading[mainloop + 1]) == True:
            target_num = (int(reading[mainloop]) + int(reading[mainloop + 1])) / 2
            target_num = int(target_num)
            # print("qwq",target_num)

            for backback in range(mainloop + 1 , -1 , -1):
                if int(reading[backback]) == target_num:
                    bro_what_happen = 0
                    break
                else:
                    bro_what_happen += 1

        if bro_what_happen > 0:
            print("NO")
            return -1
        else:
            print("YES")
            return 0

# 这个读取部分我不知道咋写,一开始当作单组输入了,完犊子。
import sys
total = sys.stdin.read().split()
for line in range(0 , len(total)):
    reading = total[line]
    reading = list(reading)
    # print(reading)
    process_part()
    del reading