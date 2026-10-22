m,n = input().split()
m = int(m)
n = int(n)

if not 1 < m < 2**31-1 or not 1 < n < 2**31-1:
    print("异常的值,请重新输入。")
    # 这个范围应该是为了照顾别的编程语言而写的设定。
    # 这里就象征性写上得了。
elif m % n == 0:
    print("YES")
    # AMD,YES
else:
    print("NO")