num = int(input("请输入一个整数："))
i = 0
while num >= 0:
    print(f"{i} + {num} = {num + i}")
    i += 1
    num -= 1

num = int(input("请输入一个整数："))
i = 0
while i <= num:
    print(f"{i} + {num - i} = {num}")
    i += 1

