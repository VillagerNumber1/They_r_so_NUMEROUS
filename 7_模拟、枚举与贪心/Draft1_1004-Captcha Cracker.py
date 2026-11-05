"""
这个出题人可以的,都考察到OCR库的使用了
不对啊这不是acm的题目咩!?
而且这个网址♂That's ♂ Good.
"""

# 检测数字是否符合题意
def testify_num(input_num):
    the_num = ['0','2','4','6','9']
    if input_num in the_num:
        return input_num
    else:
        return -1

# 检查英文对应的数字(传入的似乎是列表)
def testify_word(input_word):
    word = "".join(input_word)
    setparate_word = ['one','three','five','seven','eight']
    if len(word) <= 1:
        return -10086
    elif word in setparate_word:
        return -114514
    elif word == 'zero':
        return 0
    elif word == 'two':
        return 2
    elif word == 'four':
        return 4
    elif word == 'six':
        return 6
    elif word == 'nine':
        return 9
    else:
        # print("排查一下是否出现了错误。")
        # exit()
        return -1

# 输入部分
import sys
import time
lines = []
for line in sys.stdin.read().split():
    lines.append(line)
del line
#print(lines)

data_count = int(lines[0])
del lines[0]

for group_num in range(0 , data_count):
    group = []
    group_notlist = lines[group_num]
    group = list(group_notlist)
    # print(group)
    temp_word = []
    verify_num = []
    i = 0
    while i < len(group):
        # print(f"第一层 {i}")
        """
        思路：判断单字符是否为阿拉伯数字，若是则过

        判断单字符是否为英文，若是，进入while 循环
        通过while循环删除重复的英文元素
        然后添加进temp_word
        temp_word进入我def的函数查询阿拉伯，然后添加成密码即可
        (添加方式:用str处理，然后处理成一个整体后再导入verify word)

        好像有越界的可能，还是稍微看一下有没有更好的解法。
        """
        # 该字符是否为数字
        if 48 <= ord(group[i]) <= 57:
            # print("QwQ")
            # 性能优化先不做,我看看错误在哪里
            if int(testify_num(group[i])) >= 0:
                verify_num.append(str(testify_num(group[i])))
            i += 1

        # 那么就是英文咯
        elif 97 <= ord(group[i]) <= 122:
            if not temp_word:
                temp_word.append(group[i])
                continue
            elif temp_word:
                while i < len(group):
                    # 查重
                    # print(f"qwq : {i}")
                    # print(f"{group[i]}")
                    # time.sleep(0.05)
                    if temp_word[0] == group[i]:
                        del group[i]
                        continue
                    # 查数字(出现说明一定是终止)
                    elif temp_word[0] != group[i] and\
                    48 <= ord(group[i]) <= 57:
                        # print(testify_word(temp_word))
                        if testify_word(temp_word) >= 0:
                            verify_num.append(str(testify_word(temp_word)))
                            temp_word = []
                            break
                        else:
                            # print("???")
                            i += 1
                    # 查英文(进行持续检测,如果是个完整的英文,转数字break)
                    elif temp_word[0] != group[i] and\
                    97 <= ord(group[i]) <= 122:
                        # 长度不够,被跳过检测
                        if testify_word(temp_word) == -10086:
                            i += 1
                            continue
                        # 在黑名单里头
                        elif testify_word(temp_word) == -114514:
                            i += 1
                            temp_word = []
                            continue
    # print(f"跳出循环 {i}")
    print("".join(verify_num))