# 记录点
dot = int(input())

# 读成列表,再想想要干嘛
nums = list(map(int,input().split()))

# 特殊情况 → 列表尾巴相减 → 特殊情况2
if len(nums) == 1:
    # 本质: 是否需要分类讨论
    if nums[-1] == 15:
        print("DOWN")
        exit()
    elif nums[-1] == 0:
        print("UP")
        exit()
    else:
        print("-1")
        exit()

if len(nums) >= 2:
    if nums[-2] == 1 and nums[-1] == 0:
        print("UP")
        exit()
    elif nums[-2] == 14 and nums[-1] == 15:
        print("DOWN")
        exit()
    else:
        temp = nums[-2] - nums[-1]
        if temp <= -1:
            print("UP")
        elif temp >= 1:
            print("DOWN")