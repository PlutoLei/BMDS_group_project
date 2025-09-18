# 方法1, 调用enumerate函数
tuple_color = ('red', 'green', 'blue', 'yellow', 'white', 'black')
for idx, ele in enumerate(tuple_color):
    print(f"第{idx + 1}个元素是{ele}")

# 方法2, 使用元组的index索引方法, 即tuple.index()
tuple_color = ('red', 'green', 'blue', 'yellow', 'white', 'black')
for ele in tuple_color:
    print(f"第{tuple_color.index(ele) + 1}个元素是{ele}")


