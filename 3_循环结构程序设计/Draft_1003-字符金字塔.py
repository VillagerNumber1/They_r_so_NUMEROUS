# 对于C语言而言估计是比较好实现的。
# 跟1001有差不多的共同之处。

def space_count(space_count):
    while True:
        space_count -= 1
        print(end=" ")
        if space_count < 0:
            break

def alphabet(number):
    backup_number = number
    reverse = 0
    while True:
        char_number = number + 64
        # 输出部分
        if number > 0 and reverse == 0:
            print(chr(char_number),end="")
            number -= 1
        elif number > 0 and reverse == 1:
            print(chr(char_number),end="")
            number += 1
        # 后台处理
        if number == 0 and reverse == 0:
            reverse = 1
            number += 2
        if backup_number < number and reverse == 1:
            print(end="\n")
            break

while True:
    try:
        capture = input("")
        if capture.isalpha() == False:
            print("重写1个字母吧。")
            continue
        elif not (65 <= ord(capture) <= 90 or 97 <= ord(capture) <= 122):
            print("输入的不是字母。")
            continue
        else:
            break
    except:
        print("可能输入有误，请重试。")
if 97 <= ord(capture) <= 122:
    capture = capture.upper()

capture_ascii = ord(capture)
# 先换成数字看看什么个事情
space = capture_ascii - 65
for i in range(65 , capture_ascii + 1):
    space_count(space)
    space -= 1
    number = i - 64
    alphabet(number)