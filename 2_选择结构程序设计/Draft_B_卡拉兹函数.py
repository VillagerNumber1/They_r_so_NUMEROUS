while True:
    try:
        n = int(input(""))
        if n <= 0:
            print("输入的整数必须为正整数，请重新输入。")
            continue
            # 正整数校验
        elif n % 2 == 1:
            fn = 3*n + 1
            print(f"{int(fn)}")
            break
            # 奇数
        elif n % 2 == 0:
            fn = n / 2
            print(f"{int(fn)}")
            break
            # 偶数
    except:
        print("奇怪的值出现了。")