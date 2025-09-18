preliminary_results = float(input("初赛成绩：") )
if preliminary_results >= 8.0:
    gender = input("性别（男/女）：")
    if gender == "男":
        print("您已进入男子组决赛")
    else:
        print("您已进入女子组决赛")
else:
    print("您已被淘汰")
