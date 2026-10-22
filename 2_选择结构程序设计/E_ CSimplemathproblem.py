X,Y = input().split()
X = int(X)
Y = int(Y)

if not 1 <= X <= Y <= 100000000000000:
    print("ERROR")
elif Y % X == 0:
    # 按照百度的说法写的
    Z = int(X+Y)
    print(Z)
else:
    Z = int(Y-X)
    print(Z)