list_name = ["Jack", "Lisa", "HSP", "Paul", "Smith", "Kobe"]

# 取出前三个名字
slice_a = list_name[0:3]
print("取出前三个名字:", slice_a)

# 取出后三个名字
slice_b = list_name[-1:-4:-1]
slice_b.reverse()  # 对函数进行逆序操作
print("取出后三个名字:", slice_b)
