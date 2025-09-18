list_a = [100, 200, 300, 400, 500, 600]
print("list_a 列表元素个数:", len(list_a))
print("list_a 列表最大元素", max(list_a))
print("list_a 列表最小元素", min(list_a))

# list.append(obj) : 在列表末尾添加新的对象
# 请在list_a列表后, 添加900
list_a.append(900)
print("list_a:", list_a) #[100, 200, 300, 400, 500, 600, 900]

# list.count(obj) : 统计某个元素在列表中出现的次数
print("100出现的次数是:", list_a.count(100)) # 100出现的次数是: 1

# list.exend(seq): 在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
list_b = [1, 2, 3]
# 将list_b追加到list_a
list_a.extend(list_b)
print("list_a:", list_a) # [100, 200, 300, 400, 500, 600, 900, 1, 2, 3]

#  list.index(obj) : 从列表中找出某个值第一个匹配项的索引位置
# 如果找不到, 会报错: ValueError

# 翻转list_a, list_a.reverse()
print("300第一次出现在序列的索引是:", list_a.index(300)) # 300第一次出现在序列的索引是: 2
list_a.reverse()
print(list_a) # [3, 2, 1, 900, 600, 500, 400, 300, 200, 100]

#  list.insert(index, obj)：将对象插入到列表指定的index位置
# 请实现把666插入到index为1的位置
list_a.insert(1, 666)
print(list_a) # [3, 666, 2, 1, 900, 600, 500, 400, 300, 200, 100]

