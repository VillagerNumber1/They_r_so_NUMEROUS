lines = []

def sun_of_the_beach(year,month): # 我们需要判断日期到底有多少
    month = int(month)
    year = int(year)
    day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,9,11]
    day_28OR29 = [2]
    # 由于2月份比较特殊,这里单独判断
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29 # 闰年
        else:
            return 28 # 平年
    elif month in day_31: # 大月
        return 31
    elif month in day_30: # 小月
        return 30
    else:
        return 114514 # 不知道什么情况能返回这玩意

while True:
    try:
        # 先读取一行,并去掉两端的空格和换行
        line = input().strip()
        if line == "":
            break
        

        # 切空格,变字符串
        year,month,x = map(str,line.split())
        occurrance = 0

        if len(month) == 1:
            month = '0' + month

        day_total = sun_of_the_beach(year,month)
        day_total = str(day_total)

        if day_total == 114514:
            print("月份有误...退出码:114514")
            break

        for now_day_is in range(1,int(day_total) + 1):
            if now_day_is <= 9:
                current_now_day_is = '0' + str(now_day_is)
                statistics = year + month + current_now_day_is
            else:
                statistics = year + month + str(now_day_is)
            for i in statistics:
                if i == x:
                    occurrance += 1

        print(occurrance)
    except:
        break