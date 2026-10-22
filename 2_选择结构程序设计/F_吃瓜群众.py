weight = int(input())

# 重量判断
if not 1 <= weight <= 100:
    print("ERROR")

"""
如果西瓜分成两部分,且重量均为偶数的话。
那就需要重量为偶数...题目是啥意思?
"""
if weight % 2 == 0 and weight > 2:
    print("YES, you can divide the watermelon into two even parts.")
else:
    print("NO, you can't divide the watermelon into two even parts.")