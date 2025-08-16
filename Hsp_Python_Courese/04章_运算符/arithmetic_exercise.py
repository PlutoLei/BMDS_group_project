Total_working_days = 97
Left_weeks = Total_working_days // 7
Left_days = Total_working_days % 7
print(f"假如还有{Total_working_days}天放假，合{Left_weeks}周{Left_days}天")

hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
# 在f-strings中保留小数点后两位小数
print(f"{hua_shi}华氏温度对应的摄氏温度是{she_shi:.2f}")
