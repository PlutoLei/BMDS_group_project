'''
冒泡排序原理简述：

- 比较相邻元素，若前者大于后者则交换，使较大元素逐步“冒 ”到右侧。
- 第1轮结束后，最大元素一定在末尾；第2轮次大元素到倒数第二位，依此类推。
- 外层循环控制轮次，共进行 *n-1* 轮；内层每轮比较区间逐渐减少。
- 可提前优化：若某一轮无交换，可判定已整体有序并结束。
- 时间复杂度：最坏/平均 O(n²)，最好（已排序且加交换标志优化）O(n)。
- 空间复杂度：O(1)，原地排序；稳定性：稳定。
'''
num_list = [24, 69, 80, 57, 13, 0, 90]
print(f"排序前的列表是{num_list}")
print("排序前".center(32,"-"))

# 用i来控制整体的比较轮次
for i in range(0, len(num_list) - 1):
    # 用j来控制内部循环的比较索引
    for j in range(0, len(num_list) - 1 - i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    print(f"第{i + 1}轮比较后的list结果：{num_list}")

print("排序后".center(32,"-"))
print(f"排序后的列表是{num_list}")
