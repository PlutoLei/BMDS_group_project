# 循环从列表输入五个成绩, 保存到列表, 并输出
scores = []
# 如果只是为了循环而不使用里面的数据，用这个语句也可以 for _ in range(5):
for i in range(5):
    score = float(input("Please input your score:"))
    scores.append(score)
print("成绩情况是:", scores)