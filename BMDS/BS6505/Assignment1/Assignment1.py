# analyze_week2.py
# -*- coding: utf-8 -*-
"""
Compute measures of central tendency & variability per group,
plot boxplots, and flag outliers using the 1.5*IQR rule.

Requirements:
    pip install pandas matplotlib
Input:
    week2_data.txt  (TSV with columns: Controls, Prediabetics, T2D_Cases)
Outputs:
    summary_stats.csv
    boxplot_outliers.png
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ------------ Config ------------
INPUT_FILE = "week2_data.txt"
OUTPUT_STATS_CSV = "summary_stats.csv"
OUTPUT_BOXPLOT_PNG = "boxplot_outliers.png"

# ------------ Load data ------------
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(
        f"Could not find {INPUT_FILE}. "
        "Place this script in the same folder as week2_data.txt."
    )

# week2_data.txt is tab-separated (TSV)
df = pd.read_csv(INPUT_FILE, sep="\t")

# sanity check: ensure numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ------------ Helper: compute stats for one Series ------------
def calc_stats(s: pd.Series) -> pd.Series:
    # mode(): could be multi-modal; take the first by default if any
    mode_val = s.mode()
    mode_val = mode_val.iloc[0] if not mode_val.empty else np.nan

    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    rmin = s.min()
    rmax = s.max()

    return pd.Series(
        {
            "Mean": s.mean(),
            "Median": s.median(),
            "Mode": mode_val,
            "Std Dev": s.std(ddof=1),
            "Variance": s.var(ddof=1),
            "Min": rmin,
            "Max": rmax,
            "Range": rmax - rmin,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
        }
    )

# ------------ Compute stats for each group ------------
summary_stats = df.apply(calc_stats)
print("\n=== Summary Statistics by Group ===")
print(summary_stats.round(3))

# Save to CSV
summary_stats.to_csv(OUTPUT_STATS_CSV, float_format="%.6f")
print(f"\nSaved summary stats -> {OUTPUT_STATS_CSV}")

# ------------ Identify outliers by 1.5*IQR rule ------------
def find_outliers_iqr(s: pd.Series):
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (s < lower) | (s > upper)
    return s[mask], lower, upper

print("\n=== Outliers (1.5 × IQR rule) ===")
outliers_dict = {}
for col in df.columns:
    out_vals, lower, upper = find_outliers_iqr(df[col])
    outliers_dict[col] = {
        "outliers": list(out_vals.values),
        "lower_bound": float(lower),
        "upper_bound": float(upper),
    }
    if len(out_vals) == 0:
        print(f"- {col}: None (bounds: [{lower:.3f}, {upper:.3f}])")
    else:
        print(
            f"- {col}: {list(out_vals.values)} "
            f"(bounds: [{lower:.3f}, {upper:.3f}])"
        )

# ------------ Plot boxplot and annotate outliers ------------
# ------------ Plot boxplot and annotate outliers ------------
plt.figure(figsize=(8, 6))

# 用箱线图；关闭默认离群点显示，改为自定义标注
ax = sns.boxplot(data=df, showfliers=False, width=0.6, palette="pastel")
ax.set_title("Boxplot with Outliers (1.5 × IQR)")
ax.set_ylabel("Values")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)

# 叠加离群点（红色三角）并标注数值
for i, col in enumerate(df.columns):  # seaborn 类别坐标从 0 开始
    outs = outliers_dict[col]["outliers"]
    if len(outs) == 0:
        continue
    x_vals = np.full(len(outs), i, dtype=float)
    if len(outs) > 1:
        x_vals += np.linspace(-0.08, 0.08, len(outs))  # 轻微抖动防重叠
    plt.scatter(x_vals, outs, color="red", marker="^", s=30, zorder=5)
    for x, y in zip(x_vals, outs):
        plt.text(x, y, f"{y}", ha="center", va="bottom", fontsize=8, color="red")

plt.tight_layout()
plt.savefig(OUTPUT_BOXPLOT_PNG, dpi=150)
print(f"Saved boxplot -> {OUTPUT_BOXPLOT_PNG}")
plt.title("Boxplot with Outliers (1.5 × IQR)")
plt.ylabel("Values")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(OUTPUT_BOXPLOT_PNG, dpi=150)
print(f"Saved boxplot -> {OUTPUT_BOXPLOT_PNG}")

# Optionally show the plot when running interactively
# plt.show()