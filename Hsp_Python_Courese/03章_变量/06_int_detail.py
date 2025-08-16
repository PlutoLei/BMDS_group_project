# 字节数随着数字的增大而增大
import sys

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 3 ** 30
n6 = 2 ** 128

# 在 Python中, 可以通过sys.getsizeof返回对象(数据)的大小(按照字节单位返回)
print(n1, sys.getsizeof(n1), type(n1))
print(n2, sys.getsizeof(n2), type(n2))
print(n3, sys.getsizeof(n3), type(n3))
print(n4, sys.getsizeof(n4), type(n4))
print(n5, sys.getsizeof(n5), type(n5))
print(n6, sys.getsizeof(n6), type(n6))
