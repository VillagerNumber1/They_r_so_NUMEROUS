# 题目意思是把例如 个位 和 十位 的数字加起来。
fivefive = 0
x,y = input().split()
x = int(x)
y = int(y)

if x < y:
    for n1 in range(x , y + 1):
        i = 0
        for qwq in str(n1):
            i += int(qwq)
        if i % 5 == 0:
            fivefive += 1

elif x > y:
    for n2 in range(y , x + 1):
        i = 0
        for awa in str(n2):
            i += int(awa)
        if i % 5 == 0:
            fivefive += 1

print(fivefive)