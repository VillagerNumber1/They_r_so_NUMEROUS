# んんんんんんんんんん
import sys

lines = sys.stdin.read().split()
T = lines[0]
i = 1 # 第1组开始

while True:
    x1 = lines[-1 + 2 * i]
    x2 = lines[0 + 2 * i]
    output_x = int(x1) * int(x2)
    print(output_x)
    if i >= int(T):
        break
    i += 1