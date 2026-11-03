# 由 deepseek 编写,经过多次友好交流。
import sys

# 字典查表
bridges = {
    (1, 3): 2, (3, 1): 2, (4, 6): 5, (6, 4): 5, (7, 9): 8, (9, 7): 8,
    (1, 7): 4, (7, 1): 4, (2, 8): 5, (8, 2): 5, (3, 9): 6, (9, 3): 6,
    (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5
}

lines = sys.stdin.read().split()

for reading in lines:
    # 1. 集合查重（最优雅）
    if len(set(reading)) != len(reading):
        print("NO")
        continue

    # 2. 核心判断
    visited = set()
    is_valid = True
    
    for i in range(len(reading) - 1):
        a = int(reading[i])
        b = int(reading[i + 1])
        
        visited.add(a)
        
        # 查字典
        if (a, b) in bridges:
            if bridges[(a, b)] not in visited:
                is_valid = False
                break # 发现违规，直接跳出当前密码的判断

    # 3. 输出结果
    if is_valid:
        print("YES")
    else:
        print("NO")