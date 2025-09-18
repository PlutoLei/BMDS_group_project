tuple_movie = ('大话西游', '周星驰', 80, ['周星驰', '小甜甜'])

# 查询票价对应索引
print(f"票价对应的索引是{tuple_movie.index(80)}")

# 遍历所有的演员
for actor in (tuple_movie[3]):
    print(f"演员的名字是:{actor}")

# 删除'小甜甜', 添加演员'牛魔王'、'猪八戒'
del tuple_movie[3][1]
actor_new = ['牛魔王', '猪八戒']
tuple_movie[3].extend(actor_new)
print(tuple_movie[3])
