def peaches(days):
    """计算第days天剩余桃子数，反推第1天的桃子总数"""
    if days == 10:  # 第10天剩余1个
        return 1
    elif 1 <= days <= 9:
        return (peaches(days + 1) + 1) * 2
    else:
        raise ValueError("天数必须在1-9之间")

print(f"最初共有{peaches(1)}个桃子")