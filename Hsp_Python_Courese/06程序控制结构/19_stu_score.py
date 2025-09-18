# 定义相关的变量
# 定义班级个数
class_num = 3
# 学生的个数
student_num = 5
total = 0.0
# 统计及格人数
pass_num = 0
for j in range(1,  class_num + 1):

    # 统计1个班成绩情况, 求出一个班的平均分-for 循环5次，接受学员的成绩
    # 统计每个班的总分前，需要清0
    sum = 0.0
    for i in range(1, student_num + 1):
        score = float(input(f"请输入第{j}班第{i}个学生的成绩:"))
        # 判断成绩是否及格，累加到pass_num
        if score >= 60.0:
            pass_num += 1
        sum += score
    print(f"第{j}班的平均分是:{sum / 5}")
    # 将sum累加到total
    total += sum
# 输出所有班级的平均分和及格人数
print(f"所有班级的平均分是：{total / (student_num * class_num)}, 及格人数是{pass_num}")


