name = "Tom"  # 字符串
age = 20  # 整型
score = 90.4  # 浮点型(小数)
gender = "male"  # 字符串
is_pass = True  # bool 类型

# 查看变量的类型(本质是查看变量指向的数据的类型)
print(type(name))
print(type(age))
print(type(score))
print(type(name))
print(type(is_pass))

# type()也可以直接查看具体的值(字面量)的类型
print(f"hello的类型是{type('hello')}")
print(f"1.1的类型是{type(1.1)}")
print(f"100的类型是{type(100)}")
print(f"True的类型是{type(True)}")