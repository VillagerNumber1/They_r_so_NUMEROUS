import sys

for line in sys.stdin:
    list_qwq = line.split()
# 把输入存储成列表，然后比较大小

if list_qwq[0] < list_qwq[1]:
    print("<")
elif list_qwq[0] > list_qwq[1]:
    print(">")
elif list_qwq[0] == list_qwq[1]:
    print("=")
else:
    print("ERROR")