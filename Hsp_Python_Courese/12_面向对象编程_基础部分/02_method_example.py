class Person:
    # 属性(成员变量)
    name = None
    age = None

    def hi(self):
        print("hi, python")

    def cal01(self):
        # result = 0
        # for i in range(0, 1001):
        #     result += i
        # print(f"1 +...+1000的结果为{result}")
        result = sum([i for i in range(0, 1001)])
        print(f"1 +...+1000的结果为{result}")
        return result

    def cal02(self, n):
        result = sum([i for i in range(0, n + 1)])
        print(f"1 +...+n的结果为{result}")
        return result

    def get_sum(self, num1, num2):
        return  num1 + num2


# 测试
p = Person()
p.hi()
p.cal01()
p.cal02(10)
print(p.get_sum(10,20))