# i控制层数
for i in range(1, 10):
    if 1 <= i <= 5:
        # k控制空格数
        for k in range(5 - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * (i - 1) or i == 5:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        # 这里的 i-5 是由(5 - (10 - i))得来的
        for k in range(i - 5):
            print(" ", end="")
        for j in range(2 * (10 - i) - 1):
            if j == 0 or j == 2 * (10 - i) - 2 or i == 9:
                print("*", end="")
            else:
                print(" ", end="")
    print("")
