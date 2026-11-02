# 不好意思，老子用python

import itertools

def allPermutation(n):
    permutation = []

    for i in range(n):
        # 先把需要生成全排列的首数字放进列表
        permutation.append(i + 1)
    return list(itertools.permutations(permutation))

# 按照题目要求处理输出。
temp = str(allPermutation(8))
temp = temp.replace("), (","\n")
temp = temp.replace(",","")
temp = temp.replace("[(","")
temp = temp.replace(")]","")
print(temp)