import sys

def Istriangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a+b>c and a+c>b and b+c>a:
        # 有三角形,满意了吧。
        return True
    else:
        return False

lines = []
for line in sys.stdin.read():
    lines.append(line)

side_length = []
qwq = False
for a in range(1 , int(lines[0]) + 1):
    for b in range(1 , int(lines[0]) + 1):
        for c in range(1 , int(lines[0]) + 1):
            if a == b or a == c or b == c:
                break
            qwq = Istriangle(a,b,c)
            if qwq == True:
                temp = [a,b,c]
                temp.sort(reverse=False)
                temp = tuple(temp)
                side_length.append(temp)

if qwq == True:
    set_side_length = set(side_length)
    for i in range(0 , len(set_side_length)):
        for j in range(0 , len(set_side_length)):
            if i == j:
                continue
            if set_side_length[i]
    print(side_length)
if qwq == False:
    print("No solution")