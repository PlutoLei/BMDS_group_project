# 依赖：pandas、matplotlib
# 用途：完成Assignment1的数据分析与可视化
# 输入文件：assignment1_data.csv（列：year, facility_type_a, sex, age, rate）

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False    # 正常显示负号
from pathlib import Path

# -----------------------------
# 0) 读取与基础检查
# -----------------------------
CSV_PATH = "assignment1_data.csv"
df = pd.read_csv(CSV_PATH)

# 统一列名与类型
df.columns = [c.strip() for c in df.columns]
df["year"] = df["year"].astype(int)
df["facility_type_a"] = df["facility_type_a"].astype(str)
df["sex"] = df["sex"].astype(str)
df["age"] = df["age"].astype(str)
df["rate"] = pd.to_numeric(df["rate"], errors="coerce")

# 基础断言（可选）
assert set(df["facility_type_a"].unique()) >= {"Acute", "Psychiatric Hospitals"}, "缺少必要的机构类别"
assert set(df["sex"].unique()) <= {"Male", "Female"}, "性别列异常"
assert set(df["age"].unique()) >= {"15-64 years"}, "未找到成年人(15-64 years)年龄段"

# 创建输出目录（可选）
outdir = Path("output_q456")
outdir.mkdir(exist_ok=True)

# ============================================================
# Q4 「成年(15-64岁)在精神病院与急性医院的入院率是否随时间上升」
# ============================================================
# 口径：对 15-64 years 子集，按年×机构×性别计算 rate 的平均值；
#       同时也提供“按年×机构对男女取平均”的总体趋势。

adults = df[df["age"] == "15-64 years"].copy()

# （a）按性别的年趋势（Acute / Psychiatric Hospitals）
q4_by_sex = (
    adults[adults["facility_type_a"].isin(["Acute", "Psychiatric Hospitals"])]
    .groupby(["year", "facility_type_a", "sex"], as_index=False)["rate"]
    .mean()
    .sort_values(["facility_type_a", "sex", "year"])
)

# （b）对男女再取平均的年趋势（Acute / Psychiatric Hospitals）
q4_overall = (
    q4_by_sex.groupby(["year", "facility_type_a"], as_index=False)["rate"]
    .mean()
    .sort_values(["facility_type_a", "year"])
)

# 导出表格
q4_by_sex.to_csv(outdir / "q4_adult_trend_by_sex.csv", index=False)
q4_overall.to_csv(outdir / "q4_adult_trend_overall.csv", index=False)

# 画图1：总体（男女平均）趋势折线
plt.figure(figsize=(8, 5))
for fac in ["Acute", "Psychiatric Hospitals"]:
    sub = q4_overall[q4_overall["facility_type_a"] == fac]
    plt.plot(sub["year"], sub["rate"], marker="o", label=fac)
plt.title("Adult (15–64) Admission Rate Trend (男女平均)")
plt.xlabel("Year")
plt.ylabel("Rate per 1,000")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(outdir / "q4_adult_trend_overall.png", dpi=180)
plt.close()

# 画图2：分性别趋势（并列两条线 × 2个机构）
for fac in ["Acute", "Psychiatric Hospitals"]:
    plt.figure(figsize=(8, 5))
    for sx in ["Male", "Female"]:
        sub = q4_by_sex[(q4_by_sex["facility_type_a"] == fac) & (q4_by_sex["sex"] == sx)]
        plt.plot(sub["year"], sub["rate"], marker="o", label=sx)
    plt.title(f"Adult (15–64) Admission Rate Trend by Sex — {fac}")
    plt.xlabel("Year")
    plt.ylabel("Rate per 1,000")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outdir / f"q4_adult_trend_by_sex_{fac.replace(' ', '_')}.png", dpi=180)
    plt.close()

# ============================================================
# Q5 「男性住院率是否高于女性」
# ============================================================
# 口径：按 机构×性别 计算“跨全部年份与年龄组”的平均入院率；
#       同时输出按年细分的比较表（便于核查稳定性）。

# （a）总体（跨年、跨年龄）机构×性别 平均
q5_fac_sex_overall = (
    df.groupby(["facility_type_a", "sex"], as_index=False)["rate"]
    .mean()
    .sort_values(["facility_type_a", "sex"])
)
q5_fac_sex_overall.to_csv(outdir / "q5_facility_sex_overall_mean.csv", index=False)

# （b）按年 × 机构 × 性别 平均（可用于逐年比较）
q5_fac_sex_by_year = (
    df.groupby(["year", "facility_type_a", "sex"], as_index=False)["rate"]
    .mean()
    .sort_values(["facility_type_a", "sex", "year"])
)
q5_fac_sex_by_year.to_csv(outdir / "q5_facility_sex_by_year_mean.csv", index=False)

# 可视化：柱状图（总体）
pivot_q5 = q5_fac_sex_overall.pivot(index="facility_type_a", columns="sex", values="rate")
plt.figure(figsize=(8, 5))
pivot_q5.plot(kind="bar")
plt.title("Average Admission Rate by Facility and Sex (All years & ages)")
plt.xlabel("Facility Type")
plt.ylabel("Rate per 1,000")
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(outdir / "q5_facility_sex_bar_overall.png", dpi=180)
plt.close()

# ============================================================
# Q6 「Acute 机构下，mean 与 median 的对比（按性别×年份）」
# ============================================================
# 口径：对 Acute 机构，按 年×性别 汇总各年龄组的 mean 与 median；
#       再画出两条曲线（同一张图中分别是mean与median），对男女分别作图。

acute = df[df["facility_type_a"] == "Acute"].copy()

q6_stats = (
    acute.groupby(["year", "sex"])["rate"]
    .agg(mean="mean", median="median")
    .reset_index()
    .sort_values(["sex", "year"])
)
q6_stats["diff_mean_minus_median"] = q6_stats["mean"] - q6_stats["median"]
q6_stats.to_csv(outdir / "q6_acute_mean_vs_median_by_year_sex.csv", index=False)

# 可视化：男女各一张图（mean与median两条线）
for sx in ["Male", "Female"]:
    sub = q6_stats[q6_stats["sex"] == sx]
    plt.figure(figsize=(8, 5))
    plt.plot(sub["year"], sub["mean"], marker="o", label="Mean")
    plt.plot(sub["year"], sub["median"], marker="s", label="Median")
    plt.title(f"Acute — {sx}: Mean vs Median (by Year)")
    plt.xlabel("Year")
    plt.ylabel("Rate per 1,000")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outdir / f"q6_acute_mean_median_{sx}.png", dpi=180)
    plt.close()

print("✅ 已完成：")
print(f"- Q4: output 到 {outdir}/q4_adult_trend_overall.png 及 q4_adult_trend_by_sex_*.png")
print(f"- Q5: output 到 {outdir}/q5_facility_sex_bar_overall.png 及相关CSV")
print(f"- Q6: output 到 {outdir}/q6_acute_mean_median_Male.png / Female.png 及相关CSV")
