# 到底是为什么
# 思路参考: ac.nowcoder.com/acm/contest/view-submission?submissionId=85329592

import sys
lines = sys.stdin.read().split()
# print(lines)
count = int(lines[0])

for i in range(1 , count + 1):
    line = lines[i]
    if not line:
        print(end="\n")
        continue

    point = 0
    result = []
    while point < len(line):
        reading = line[point]

        if reading in ["0","2","4","6","9"]:
            result.append(str(reading))
            point += 1
        elif line.startswith("zero", point):
            result.append("0")
            point += 4
        elif line.startswith("two", point):
            result.append("2")
            point += 3
        elif line.startswith("four", point):
            result.append("4")
            point += 4
        elif line.startswith("six", point):
            result.append("6")
            point += 3
        elif line.startswith("nine", point):
            result.append("9")
            point += 4
        else:
            point += 1

    print("".join(result))