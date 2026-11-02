import sys

def Istriangle(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a+b>c and a+c>b and b+c>a:
        # 有三角形,满意了吧。
        return True
    else:
        return False

lines = []
for line in sys.stdin.read().split():
    lines.append(line)

# 老实说这个处理部分没有优化, 数学这块是我的弱项。
side_length = []
side_length = set(side_length)
qwq = False
for a in range(1 , int(lines[0]) + 1):
    for b in range(a + 1 , int(lines[0]) + 1):
        for c in range(b + 1 , int(lines[0]) + 1):
            if Istriangle(lines[a],lines[b],lines[c]) == True:
                temp = [int(lines[a]),int(lines[b]),int(lines[c])]
                temp.sort(reverse=False)
                temp = tuple(temp)
                side_length.add(temp)
                del temp

# 输出部分
if side_length:
    side_length = list(side_length)
    side_length.sort(reverse=False)
    output = side_length[-1]
    output = str(output)
    output = output.replace("), (","\n")
    output = output.replace("[(","")
    output = output.replace(")]","")
    output = output.replace(",","")
    output = output.replace("(","")
    output = output.replace(")","")
    print(output)
else:
    print("No solution")