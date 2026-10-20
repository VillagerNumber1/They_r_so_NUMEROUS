def read_circle_count(target_count):
    read_len = len(str(target_count)) - 1
    target_count = str(target_count)
    one = target_count[-1]
    ten = target_count[-2]
    hundred = target_count[-3]
    thousand = target_count[-4]
    while True:
        if target_count[-1] != target_count[-2]\
        and target_count[-1] != target_count[-3]\
        and target_count[-1] != target_count[-4]\
        and target_count[-2] != target_count[-3]\
        and target_count[-2] != target_count[-4]\
        and target_count[-3] != target_count[-4]:
            return 1
        else:
            return 0
        break

i1 = 0
i2 = 0
i3 = 0
for i1 in range(1000,9999):
    for i2 in range(1,100):
        for i3 in range(1,100):
            if i1 == i2 * i3 and i2 < i3:
                if read_circle_count(i1) == 1:
                    print(i1,"=",i2,"*",i3)
                else:
                    continue