import sys
import functools

def compare(a , b):
    # 注意是字符串拼接比较
    if a + b > b + a:
        return -1
    else:
        return 1

lines = []
for line in sys.stdin.read().split():
    lines.append(str(line))
del line

total_num = lines[0]
del lines[0]

lines.sort(key=functools.cmp_to_key(compare))

print("".join(lines))