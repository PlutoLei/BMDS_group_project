# 出票系统，根据旺季的月份和年龄，打印票价
# season_num = int(input("请输入月份(1-12)："))
# if 1 <= season_num <= 12:
#     style = input("请输入游客类型\n成人(18-60)\n儿童(<18)\n老人(>60)\n")
#     if 4 <= season_num <= 10:
#         print("4-10 旺季：")
#         if style == "成人":
#             print("\t成人(18-60):60")
#         elif style == "儿童":
#             print("\t儿童(<18):半价")
#         else:
#             print("\t老人(>60):1/3")
#     else:
#         print("淡季：")
#         if style == "成人":
#             print("\t成人：40")
#         else:
#             print("\t其他：20")

# version 2
month = int(input("请输入月份："))
age = int(input("请输入年龄："))
if 4 <= month <= 12:
    if age > 60:
        print("价格为20¥")
    elif age >= 18:
        print("价格为60¥")
    else:
        print("价格为30¥")
else:
    if 18 <= age <= 60:
        print("价格为40¥")
    else:
        print("价格为20¥")