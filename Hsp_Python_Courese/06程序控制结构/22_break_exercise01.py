#  定义sum累加和
sum = 0

# 遍历1-100
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print(f"此时当前循环控制的变量值是{i}")

