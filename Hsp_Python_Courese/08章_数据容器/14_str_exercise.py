str_names = "tom jack mary nono smith hsp"
str_names_list = str_names.split(" ")
print(f"一共有{len(str_names_list)}个人名")

new_str_names = str_names.replace("hsp", "老韩")
print(new_str_names)

str_names_upper = ""
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize() +" "

# 去掉两边的" "
str_names_upper= str_names_upper.strip(" ")
print(f"如果人名是英文，则把首字母大写，处理结果是：{str_names_upper}")
