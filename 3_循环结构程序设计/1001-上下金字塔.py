import time

getting = input().split()
i = len(getting)
for ii in getting:
    if not 2 <= int(ii) <= 9:
        print("并非2<=n<=9,退出程序")
        exit()

for ii in getting:
    ii = int(ii)
    space_len = ii - 1
    tower_note = 1

    while True: #上金字塔
        time.sleep(0.05)
        print(" "*space_len,end="")
        space_len -= 1
        print("*"*tower_note,end="")
        tower_note += 2
        print(end="\n")
        if space_len < 0:
            space_len += 1
            tower_note -= 2
            while True:
                time.sleep(0.05)
                space_len += 1
                print(" "*space_len,end="")
                tower_note -= 2
                print("*"*tower_note,end="")
                print(end="\n")
                if space_len == ii + 1:
                    break
            if space_len == ii + 1:
                break
# 因为 for 循环用的不习惯,遂用while