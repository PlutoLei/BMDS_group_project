import random
  
num_list = [random.randint(1, 100) for _ in range(10)]
print(f"随机生成的原始列表{num_list}")
print("排序后".center(51, "-"))

# 用j来控制整体循环的比较轮次
for j in range(0, len(num_list) - 1):
    # 用i来控制每个轮次里索引的移动次数(比较次数)
    for i in range(0, len(num_list) - 1 - j):
        if num_list[i] < num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
print(f"排序后的结果是{num_list}")


def binary_search(my_list, find_val):
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = my_list[mid]
        if find_val < mid_val:
            left = mid + 1
        elif find_val > mid_val:
            right = mid - 1
        else:
            return mid
        return -1

# 测试
test_source = binary_search(num_list, 32)
if test_source == -1:
    print("没有找到这个数")
else:
    print(f"这个数对应的索引是{test_source}")

