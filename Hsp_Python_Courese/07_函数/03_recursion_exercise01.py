def fnb(n):
    """
    功能；返回n对应的斐波那契数
    n: 接受一个整数 n >= 1
    renturn: 返回斐波那契数
    """
    if n in (1, 2):
        return 1
    elif n > 2:
        return fnb(n - 1) + fnb(n - 2)
    return None


result = fnb(4) 
print(result)
