"""
这个出题人可以的,都考察到OCR库的使用了
不对啊这不是acm的题目咩!?
而且这个网址♂That's ♂ Good.
"""

# 输入部分
import sys
lines = []
for line in sys.stdin.read().split():
    lines.append(line)
del line
#print(lines)

data_count = lines[0]
del lines[0]

for group in lines:
    temp_word = []
    verify_word = []
    for i in range(0 , len(group)):
        """
        思路：判断单字符是否为阿拉伯数字，若是则过

        判断单字符是否为英文，若是，进入while 循环
        通过while循环删除重复的英文元素
        然后添加进temp_word
        temp_word进入我def的函数查询阿拉伯，然后添加成密码即可
        (添加方式:用str处理，然后处理成一个整体后再导入verify word)

        好像有越界的可能，还是稍微看一下有没有更好的解法。
        """