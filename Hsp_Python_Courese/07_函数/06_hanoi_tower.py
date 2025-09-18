def hanoi_tower(n, source, target, auxiliary):
    """
    汉诺塔递归解决方案
    :param n: 盘子数量
    :param source: 源柱子
    :param target: 目标柱子
    :param auxiliary: 辅助柱子
    """
    if n == 1:
        print(f"将盘子1从{source} -> {target}")
    else:
        # 有多个盘子，我们认为只有两个，也就是上面所有的盘和最下面的盘,先将上面的盘由source移动到auxiliary，中间需要target的辅助
        hanoi_tower(n - 1, source, auxiliary, target)
        # 将最下面的盘子(最大目标盘子)从 source 移动到 target
        print(f"将盘子{n}从{source} -> {target}")
        # 将auxiliary上的所有盘子移动到target，中间需要source的帮助
        hanoi_tower(n - 1, auxiliary, target, source)


hanoi_tower(3, "A", "B", "C")
