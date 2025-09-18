i = 1
max_num = 100
count = 0
sum = 0
while i <= 100:
    if i % 9 == 0:
        print(i)
        count += 1
        sum += i
    i += 1
print(f"100以内能被9整除的数共有{count}个，他们的总和为{sum}")

