str_b = "hi-韩顺平教育"
# while循环
index = 0
while index < len(str_b):
    print(f"第{index + 1}个元素是 -> {str_b[index]}")
    index += 1

print("=" * 15)

# for循环
for ele in str_b:
    print(f"第{str_b.index(ele) + 1}个元素是 -> {ele}")
