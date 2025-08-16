a = 10
b = 20
c = 30
max1 = a if a > b else b
max2 = b if b > c else c
max = max1 if max1 > max2 else max2
print(f"max = {max}")
