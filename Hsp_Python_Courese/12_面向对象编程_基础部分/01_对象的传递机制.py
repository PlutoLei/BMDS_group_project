class Person:
    age = None
    name = None


p1 = Person()
p1.age = 10
p1.name = "小明"
p2 = p1 # 把p1赋给了p2,即：让p2指向p1
print(p2.age) # p2.age是多少
print(f"p1.name的地址:{id(p1.name)}p2.name的地址:{id(p2.name)}")
