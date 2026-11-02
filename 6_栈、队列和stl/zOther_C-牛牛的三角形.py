n = int(input())
a = list(map(int, input().split()))

a.sort()

found = False

for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        print(a[i], a[i + 1], a[i + 2])
        found = True
        break

if not found:
    print("No solution")