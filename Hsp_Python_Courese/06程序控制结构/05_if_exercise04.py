num1 = 6
num2 = 9
if (num1 + num2) % 3 == 0 and (num1 + num2) % 5 == 0:
    print(f"{num1 + num2}既可以被3整除，也可以被5整除")
else:
    print(f"{num1 + num2}不满足既可以被3整除，又可以被5整除")
