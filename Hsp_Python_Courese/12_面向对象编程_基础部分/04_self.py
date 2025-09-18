class Dog:
    def __init__(self, name="藏獒", age=2):
        self.name = name
        self.age = age

    def info(self, other_name):
        print(f"传入的name: {other_name}")
        print(f"对象的name: {self.name}")

    def eat(self):
        print(f"{self.name} 饿了..")

    def cry(self, other_name):
        print(f"{other_name} is crying")
        print(f"{self.name} is crying")
        self.eat()

    @staticmethod
    def ok():
        print("ok()...")


# 演示self的使用
print("=== 演示1: 访问对象属性 ===")
dog1 = Dog("波斯猫")
dog1.info("加菲猫")

print("\n=== 演示2: self代表当前对象 ===")
dog2 = Dog("藏獒", 3)
print(f"dog2对象ID: {id(dog2)}")
print(f"self ID: {id(dog2)}")

print("\n=== 演示3: 方法内调用其他方法 ===")
dog3 = Dog("中华田园犬")
dog3.cry("金毛")

print("\n=== 演示4: 静态方法调用 ===")
dog3.ok()
Dog.ok()


