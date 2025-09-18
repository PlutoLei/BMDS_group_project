books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
book = dict(zip(authors, books))
print(book)

english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
dict_color = dict(zip(chinese_list, (str.upper(color) for color in english_list)))
print(dict_color)