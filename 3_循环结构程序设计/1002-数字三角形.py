import time
n = int(input())
if not 1 <= n <= 1000:
    print("Boom!")
    exit(114514)
number = 1

for line in range(1 , n + 1):
    for rank in range(1 , line + 1):
        print(f"%4d" %number ,end="")
        # 蚌埠住了,返璞归真。
        number += 1
    print(end="\n")