# 总层数
total_level = 5
# i 控制层数
for i in range(1, total_level + 1):
    # k 控制空格数
    for k in range(total_level - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * (i - 1) or i == total_level:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
