import sys
# 防御性编程还是算了,老毛病了qwq
for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue

    num = int(line)
    backup_num = num
    """
    易错点: 千万不要用for读取字符串
    因为这个bug排查了接近2个小时
    它会把"10"拆分成"1"和"0"
    卧槽血的教训

    但是讲真，太黑箱了，压根不知道系统输入的啥子！
    不过既然是系统统一输入，那么就不会刻意输入异常数据。
    血的教训。
    """

    for count in range(1 , backup_num + 2):
        # 空格
        print(" "*num*2,end="")
        # 星星眼
        print("*"*count,end="")
        # what's up
        print(end="\n")
        num -= 1

    num += 1

    for count in range(backup_num , 0 , -1):
        num += 1
        # 空格
        print(" "*num*2,end="")
        # 星星眼
        print("*"*count,end="")
        # what's up
        print(end="\n")