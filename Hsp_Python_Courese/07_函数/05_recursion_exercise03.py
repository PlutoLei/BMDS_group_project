def f(n):
    if n == 1:
        return 3
    else:
        return 2 * f(n - 1) + 1


result = f(3)
print(f"当n = {3}时，f(n)的结果是{result}")
