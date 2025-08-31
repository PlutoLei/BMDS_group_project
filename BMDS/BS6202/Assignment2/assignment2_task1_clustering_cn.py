#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
作业2 - 任务1: 基因表达聚类
----------------------------------------------------
输入:
  - /mnt/data/data.csv
  - /mnt/data/Meta_data.csv
输出 (./outputs_task1):
  - pca_scree.png
  - pca_scatter_pc1_pc2.png
  - kmeans_silhouette_vs_k.png
  - kmeans_clusters_pc1_pc2_k{best_k}.png
  - cluster_eval.csv
  - summary_task1.txt
"""

import os
os.environ["OMP_NUM_THREADS"] = "1"      # 限制 OpenMP 线程
os.environ["MKL_NUM_THREADS"] = "1"      # (可选) 限制 MKL 线程, 进一步保持一致
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

RNG = 42
OUTDIR = "./outputs_task1"
os.makedirs(OUTDIR, exist_ok=True)

# -------------------------------
# 加载数据
# -------------------------------
expr = pd.read_csv("data.csv").set_index("ID_REF")
meta = pd.read_csv("Meta_data.csv").set_index("filename")

# Align samples present in both
common = [c for c in expr.columns if c in meta.index]
expr = expr[common]
meta = meta.loc[common]

# -------------------------------
# 数据预处理: log2转换 + 基因水平Z分数标准化
# -------------------------------
expr_log2 = np.log2(expr + 1.0)
X = expr_log2.T  # samples x genes
X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=0)
X = X.replace([np.inf, -np.inf], np.nan).fillna(0.0)

# -------------------------------
# 主成分分析 (PCA)
# -------------------------------
max_pcs = min(50, X.shape[1])
pca = PCA(n_components=max_pcs, random_state=RNG)
X_pcs = pca.fit_transform(X.values)
cumvar = np.cumsum(pca.explained_variance_ratio_)
n90 = int(np.searchsorted(cumvar, 0.90) + 1)
n90 = max(n90, 2)

# Scree plot
plt.figure()
plt.plot(np.arange(1, len(cumvar)+1), cumvar, marker='o')
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA Scree Plot (Cumulative Variance)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "pca_scree.png"), dpi=160)
plt.close()

# PC1 vs PC2 scatter colored by sex (0/1)
y = meta["sex"].map({"F":0,"M":1}).values
plt.figure()
plt.scatter(X_pcs[:,0], X_pcs[:,1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Scatter (PC1 vs PC2)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "pca_scatter_pc1_pc2.png"), dpi=160)
plt.close()

# -------------------------------
# 在前n90个主成分上进行聚类
# -------------------------------
pcs = X_pcs[:, :n90]

rows = []
models = {}
for k in [2,3,4,5,6,7,8]:
    km = KMeans(n_clusters=k, random_state=RNG, n_init=20)
    labels = km.fit_predict(pcs)
    sil = silhouette_score(pcs, labels, metric='euclidean')
    ch = calinski_harabasz_score(pcs, labels)
    db = davies_bouldin_score(pcs, labels)
    rows.append({"K":k,"silhouette":sil,"calinski_harabasz":ch,"davies_bouldin":db})
    models[k] = km

eval_df = pd.DataFrame(rows)
eval_df.to_csv(os.path.join(OUTDIR, "cluster_eval.csv"), index=False)

# Silhouette vs K
plt.figure()
plt.plot(eval_df["K"], eval_df["silhouette"], marker='o')
plt.xlabel("K")
plt.ylabel("Silhouette Score")
plt.title("KMeans: Silhouette vs K")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "kmeans_silhouette_vs_k.png"), dpi=160)
plt.close()

# 最优K值
best_k = int(eval_df.loc[eval_df["silhouette"].idxmax(), "K"])
best_labels = models[best_k].labels_

# 在PC1/PC2空间可视化聚类结果
plt.figure()
plt.scatter(X_pcs[:,0], X_pcs[:,1], c=best_labels)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title(f"KMeans Clusters (K={best_k}) on PC1 vs PC2")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, f"kmeans_clusters_pc1_pc2_k{best_k}.png"), dpi=160)
plt.close()

# 层次聚类基线
agg = AgglomerativeClustering(n_clusters=2, linkage='ward')
agg_labels = agg.fit_predict(pcs)
agg_sil = silhouette_score(pcs, agg_labels, metric='euclidean')

# 汇总结果
with open(os.path.join(OUTDIR, "summary_task1.txt"), "w", encoding="utf-8") as f:
    f.write("=== TASK 1: Clustering Summary ===\n")
    f.write(f"Samples: {X.shape[0]}, Genes: {X.shape[1]}\n")
    f.write(f"PCs for ~90% variance: {n90}\n")
    f.write(f"Best K (KMeans by silhouette): {best_k}\n")
    f.write(f"Agglomerative (K=2) silhouette: {agg_sil:.4f}\n")
print("Task 1 completed.")