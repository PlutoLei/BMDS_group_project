import random

num_list = [random.randint(1, 100) for _ in range(10)]
print(f"随机生成的原始列表{num_list}")
print("排序后".center(51, "-"))

# 用j来控制整体比较轮数
for j in range(0, len(num_list) - 1):
    # 用i来控制每轮内部下标索引移动次数
    for i in range(0, len(num_list) - 1 - j):
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

print(f"冒泡排序之后的列表{num_list}")


# 二分查找列表中的某个值
def binary_search(my_list, find_val):
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = my_list[mid]
        if find_val < mid_val:
            right = mid - 1
        elif find_val > mid_val:
            left = mid + 1
        else:
            return mid
    return -1


# 测试二分查找
test_search = binary_search(num_list, 87)
if test_search == -1:
    print("没有在列表中找到这个值")
else:
    print(f"找到了对应值, 对应索引下标为{test_search}")
