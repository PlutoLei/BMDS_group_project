"""
    二分查找的思路分析
    前提: 该列表是一个排好序的列表(为了分析方便, 就以从小到大的列表为例分析)
    1. 找到列表的中间数 mid_val 和 find_val 比较
    2. 如果mid_val > find_val , 则到 mid_val的左边查找
    3. 如果mid_val < find_val , 则到 mid_val的右边查找
    4. 如果mid_val == find_val , 则到 找到，返回对应的下标即可
    5. 不断的重复 1-4步骤， 这里就是不断的折半, 使用while
    6. 如果while 结束，都没有找到, 说明find_val 没有在列表

"""

# 要查找的列表
# num_list = [1, 8, 10, 89, 1000, 1234]
num_list = [1234, 1000, 89, 10, 8, 1]

def binary_search(my_list, find_val):
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = my_list[mid]
        if find_val > mid_val:
        # 1.find_val < mid_val, 去mid_val的左边查找
            right = mid - 1
        # 1.find_val > mid_val, 去mid_val的右边查找
        elif find_val < mid_val:
            left = mid + 1
        else: # 相等
            return mid
    return -1



# 测试
result = binary_search(num_list, 89)
if result == -1:
    print(f"没有找到结果, 返回值为{result}")
else:
    print(f"找到数, 对应的下标是{result}")
