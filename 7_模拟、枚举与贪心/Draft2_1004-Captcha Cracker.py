# 重构(wdnmd)

I_Miss_You_Dictionary = {
    'zero':'0','two':'2','four':'4',
    'six':'6','nine':'9'
}
MY_DIVORCE_IS_WELL = {
    'one':'1','three':'3','five':'5',
    'seven':'7','eight':'8'
}

# 数字筛选
def filter_num(input_num):
    filter = ['0','2','4','6','9']
    if input_num in filter:
        return input_num
    else:
        return -1

# 输入处理
import sys
lines = []
for line in sys.stdin.read().split():
    lines.append(line)
# 可以改成 input_data = sys.stdin.read().split()
group_num = int(lines[0])
del line
del lines[0]
# ↑不建议用,数组的变化莫测,建议改掉这个习惯


# 进行循环检测
for now_group_num in range(0 , group_num + 0):
    process = lines[now_group_num]
    result = []
    i = 0
    while i < len(process):
        char = process[i]

        # 如果是数字的话
        if 48 <= ord(char) <= 57:
            if filter_num(char) != -1:
                result.append(char)
            i += 1
            # 思路很妙,不需要全写出else等等,
            # 只需要判断是否输进result即可,不用管i的位置。
        
        elif 97 <= ord(char) <= 122:
            matched = False
            temp = []
            # 假设找到了能匹配到的单词
            for word in I_Miss_You_Dictionary:
                if process[i:i+len(word)] == word:
                    result.append(I_Miss_You_Dictionary[word])
                    i += len(word)
                    matched = True
                    break

            # 在丢弃的单词中寻找
            if not matched:
                for word in MY_DIVORCE_IS_WELL:
                    if process[i:i+len(word)] == word:
                        i += len(word)
                        matched = True
                        break

            if not matched:
                i += 1

    print("".join(result))