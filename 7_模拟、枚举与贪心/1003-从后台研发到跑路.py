"""
思路整理:
注释为 /* */ ，去掉符号跟里面的注释
但是/*内出现了/*，当成字符串处理
抑或是*/*/中,后者作为字符串处理

单独的/*或*/当成字符串

双引号 " " 内的内容全部不能去掉
\" 情况是被视为正常字符串

参考: ac.nowcoder.com/acm/contest/view-submission?submissionId=85371259
"""

# 输入部分
import sys
code_note = sys.stdin.read()

# 尝试使用指针进行移动
i = 0
string_len = len(code_note)
result = []
in_the_note = False

while i < string_len:
    # 在双引号里面
    if in_the_note == True:
        # 处理 \" 的情况
        if i < string_len - 1 and \
        str(code_note[i])\
        + str(code_note[i + 1]) == r'\"':
            result.append(r'\"')
            i += 2
            continue
        result.append(code_note[i]) # 2333
        if code_note[i] == '"':
            in_the_note = False
        i += 1

    # 遇到了双引号(注: 不会重复,前面已经执行了)
    elif code_note[i] == '"':
        in_the_note = True
        result.append('"')
        i += 1

    # 处理 \" 的情况
    elif i < string_len - 1 and \
    str(code_note[i])\
    + str(code_note[i + 1]) == r'\"':
        result.append(r'\"')
        i += 2

    # 检测注释存在与否(不用担心双引号,前面已经排除了)
    # 谁教我语文...为什么注释内的双引号不用理会的
    elif code_note[i:i + 2] == "/*":
        # 这辈子我可想不到这种写法,太巧妙了
        j = code_note.find("*/", i + 2)
        if j == -1:
            result.append("/*")
            i += 2
        else:
            i = j + 2

    # 发现都没有,直接加入列表
    else:
        result.append(code_note[i])
        i += 1

print("".join(result))