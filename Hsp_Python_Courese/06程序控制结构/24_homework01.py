# 老韩做法
# 定义变量money = 100000 表示钱的数量
money = 100000
# 定义变量count = 0用来统计经过了多少个路口
count = 0
while True:
    # 当现金 > 50000时, 每次交5%
    if money > 50000:
        count += 1
        money -= money * 0.05
    # 当现金 <= 50000时, 每次交1000
    elif money >= 1000:
        count += 1
        money -= 1000

    else:
        break
print(f"该人一共可以经过{count}次路口, 还剩下{money}元钱")
