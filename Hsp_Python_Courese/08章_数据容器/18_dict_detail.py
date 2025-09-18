dict_b = {'one': 1, 'two': 2, 'three': 3}

# 遍历方式1-依次取出key, 再通过dict[key]取出对应的value
for key in dict_b:
    print(f"key:{key}, value:{dict_b[key]}")

# 遍历方式2-依次取出value
for value in dict_b.values():
    print(f"value:{value}")

# 遍历方式3-依次取出key-value
for k, v in dict_b.items():
    print(f"key:{k}, value:{v}")

print(dict_b.keys())
