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

# 对列表内数字部分转换成int
for lines in initial_score_list:
    if not initial_score_list[lines] == ".":
        initial_score_list[lines] = int(initial_score_list[lines])
del lines

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
dot_count = dot + 1
while t >= t_count and dot <= dot_count:
    # 四舍五入
    for i in range(dot + 1 , len(initial_score_list)):
        if i >= 5:
            initial_score_list[i] = 0
            if initial_score_list[i-1] == ".":
                initial_score_list[i-2] += 1
                break
            else:
                initial_score_list[i-1] += 1
                break
    del i

    # 对变成10的部分转换
    for i in range(-1 , -len(initial_score_list) - 1 , -1):
        if initial_score_list[i] == 10:
            initial_score_list[i] = 0
            if initial_score_list[i - 1] == ".":
                initial_score_list[i - 2] += 1
            else:
                initial_score_list[i - 1] += 1
    del i

    # 先复制列表,再进行字符串拼接
    temp_initial_score_list = initial_score_list.copy()
    for item in temp_initial_score_list:
        result = str(result)
        result += str(item) + ' '
        result = result.strip(' ')
        print(result)

    # 超次数计算
    t_count += 1