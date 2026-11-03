import sys

# 读取部分
lines = []
for line in sys.stdin.read().split():
    lines.append(line)
n = int(lines[0])
t = int(lines[1])
initial_score = lines[2]
initial_score_list = list(initial_score)
del lines


"""
定时炸弹步 → 转int
"""
# # 对列表内数字部分转换成int
# for lines in range(len(initial_score_list)):
#     if initial_score_list[lines] != ".":
#         initial_score_list[lines] = int(initial_score_list[lines])
# del lines


# 查找小数点所在位置
dot = -1
for i in range(len(initial_score_list)):
    if initial_score_list[i] == ".":
        dot = i
        break
del i

if dot == -1:
    print(initial_score)
    exit()

# 查找能四舍五入的数字
t_count = 0
while t > t_count:
    jinwei = False # 判断这轮循环是否有元素变 10

    # 四舍五入
    for i in range(dot + 1 , len(initial_score_list)):
        if int(initial_score_list[i]) >= 5:
            # 四舍五入后直接丢弃之后的元素。
            initial_score_list = initial_score_list[:i]

            j = i - 1 # j 是i之前的索引,想办法进位
            while j >= 0:
                if initial_score_list[j] == ".":
                    j -= 1 # 小数点跳过
                    continue

                # 处理四舍五入遇到变10的情况,即十六进制A
                if initial_score_list[j] == '9':
                    initial_score_list[j] = '0'
                    j -= 1
                else:
                    initial_score_list[j] = str(int(initial_score_list[j]) + 1)
                    break

            if j < 0: # 进位超了,即9.9 -> 10.0
                initial_score_list.insert(0,'1')
                dot += 1 # 细节:小数点后移

            jinwei = True
            break

    if jinwei == False:
        break

    # 超次数计算
    t_count += 1

# 字符串拼接
result = "".join(initial_score_list).strip()
result = str(result).replace("[","")\
    .replace("]","").replace("'","")\
    .replace(",","").replace(" ","")
if '.' in result:
    result = result.rstrip('0').rstrip('.')
print(result)