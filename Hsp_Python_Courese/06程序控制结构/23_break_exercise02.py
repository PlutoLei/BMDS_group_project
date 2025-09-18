for i in range(1, 4):
    name = input("请输入用户名:")
    code = int(input("请输入密码:"))
    if name == "张无忌" and code == 888:
        print("登录成功！")
        break
    elif 1 <= i <= 3:
        print(f"你还有 {3 - i} 次登录机会")
    else:
        break
