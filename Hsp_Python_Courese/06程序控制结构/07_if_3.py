score = int(input("小头儿子的期末成绩是："))
if 0 <= score <= 100:
    if score == 100:
        print("奖励小头儿子一辆BMW")
    elif 80 < score <= 90:
        print("奖励儿子一个Iphone13")
    elif 60 <= score <= 80:
        print("奖励儿子一个Ipad")
    else:
        print("啥都没有")
else:
    print("不在0~100内")