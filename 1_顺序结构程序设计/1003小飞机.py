import time
time.sleep(1.8)

# 第一列启动
j = 1
for j in range(1,7):
    if j <= 2:
        for count in range(1,6):
            print(" ",end="")
        for count in range(1,3):
            print("*",end="")
        for count in range(1,6):
            print(" ",end="")
        print("\n",end="")
    elif j <= 4 and j > 2:
        for count in range(1,13):
            print("*",end="")
        print("\n",end="")
    elif j <= 6 and j > 4:
        for count in range(1,5):
            print(" ",end="")
        print("*",end="")
        for count in range(1,3):
            print(" ",end="")
        print("*",end="")
        for count in range(1,5):
            print(" ",end="")
        print("\n",end="")
    else:
        print("???")
        exit(114514)