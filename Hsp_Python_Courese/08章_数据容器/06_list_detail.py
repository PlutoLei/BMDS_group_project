# 扩展一下, 列表在赋值的特点, 示意图说明
list1 = [1, 2.1, '韩顺平教育']
list2 = list1
list2[0] = 500
print("list2 =", list2)  # 输出[500, 2.1, '韩顺平教育']
print("list1 =", list1)  # 输出[500, 2.1, '韩顺平教育']

# 扩展一下, 看看列表在函数传参时的特点, 示意图
def f1(l):
    l[0] = 100
    print("l的id:", id(l))

list10 = [1, 2.1, 200]
print("list10的id:", id(list10))
f1(list10)
print("list10:", list10)
