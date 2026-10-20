# 这道题可太经典了。
"""
#   # #   #  ###  #####     ### #   # ####   ###   #### #####
#   # #   # #   #   #        #  ## ## #   # #   # #       #
# # # ##### #####   #        #  # # # ####  ##### #       #
## ## #   # #   #   #        #  #   # #     #   # #       #
#   # #   # #   #   #       ### #   # #     #   #  ####   #
"""


for i in range(1,10):
    for j in range(1,10):
        if i >= j and i <= 3:
            print(f"{j}*{i}= {i*j} ",end="")
        elif i >= j and i > 3:
            print(f"{j}*{i}=",end="")
            if j == 1:
                print(f" {i*j} ",end="")
            elif j == 2 and i == 4:
                print(f" {i*j} ",end="")
            else:
                print(f"{i*j} ",end="")
        if i > j:
             print("",end="")
    print(end="\n")

# 预期输出来讲, 如果这样子搞真是让人心凉了半截。