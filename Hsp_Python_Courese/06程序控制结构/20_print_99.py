# 先用i定义九九乘法表的层数
for i in range(1, 10):
    # 用j控制乘法表的行数
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j}\t", end="")
    print("")
