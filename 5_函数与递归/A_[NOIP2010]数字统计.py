L,R = map(int,input().split())

listBro = []
total = 0

for num in range(L,R+1):
    listBro.append(num)

# 数据处理部分
for now_num in range(0 , len(listBro)):
    temp_num = listBro[now_num]
    temp_num = str(temp_num)
    for string_num in range(0 , len(temp_num)):
        if int(temp_num[string_num]) == 2: # 题目说2我才2的！
            total += 1
print(total)