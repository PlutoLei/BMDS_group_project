import random
# 定义变量count，统计一共用了多少次，count += 1
count = 0
while True:
    # 生成随机数
    n = random.randint(1, 100)
    # 统计次数
    count += 1
    print(f"第{count}次：n = {n} ")
    if n == 97:
        print(f"生成97一共用了{count}次")
        break

