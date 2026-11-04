import sys
code_note = sys.stdin.read()
i = 0 # 指针
n = len(code_note)
result = [] # 储存代码
in_the_note_states = False

while i < n:
    # 对 \" 的处理
    if i < n - 1 and (code_note[i] + code_note[i+1]) == r'\"':
        result.append(i)
        i += 2

    # 如果出现了 /*
    if i < n - 1 and (code_note[i] + code_note[i+1]) == r'/*':
        in_the_note_states = True
        while (i < n - 1):
            # 对 \" 的处理
            if i < n - 1 and (code_note[i] + code_note[i+1]) == r'\"':
                i += 2
            # 若出现了双引号
            elif i < n - 1 and code_note[i] == r'"':
                quotations = i
                while quotations < n - 1:
                    # 对 \" 的处理
                    if quotations < n - 1 and (code_note[i] + code_note[i+1]) == r'\"':
                        quotations += 2
                    elif quotations < n - 1 and code_note[i] == '"':
                        
