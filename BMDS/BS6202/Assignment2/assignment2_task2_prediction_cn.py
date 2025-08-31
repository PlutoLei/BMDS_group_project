#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
作业2 - 任务2: 基于基因表达预测性别
---------------------------------------------------------
输入:
  - /mnt/data/data.csv
  - /mnt/data/Meta_data.csv
输出 (./outputs_task2):
  - roc_curves.png
  - confusion_matrix_logreg.png
  - confusion_matrix_rf.png
  - confusion_matrix_svm.png
  - metrics_task2.txt
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, roc_auc_score, roc_curve, confusion_matrix
)

RNG = 42
OUTDIR = "./outputs_task2"
os.makedirs(OUTDIR, exist_ok=True)

# -------------------------------
# 加载数据
# -------------------------------
expr = pd.read_csv("data.csv").set_index("ID_REF")
meta = pd.read_csv("Meta_data.csv").set_index("filename")

common = [c for c in expr.columns if c in meta.index]
expr = expr[common]
meta = meta.loc[common]

y = meta["sex"].map({"F":0, "M":1}).values

# -------------------------------
# 数据预处理 + PCA降维
# -------------------------------
expr_log2 = np.log2(expr + 1.0)
X = expr_log2.T
X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=0)
X = X.replace([np.inf, -np.inf], np.nan).fillna(0.0)

pca = PCA(n_components=min(50, X.shape[1]), random_state=RNG)
X_pcs = pca.fit_transform(X.values)
cumvar = np.cumsum(pca.explained_variance_ratio_)
n90 = int(np.searchsorted(cumvar, 0.90) + 1)
n90 = max(n90, 2)

X_red = X_pcs[:, :n90]

# -------------------------------
# 训练集 / 测试集划分
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_red, y, test_size=0.2, random_state=RNG, stratify=y
)

# -------------------------------
# 训练模型
# -------------------------------
lr = LogisticRegression(max_iter=500, random_state=RNG)
rf = RandomForestClassifier(n_estimators=300, random_state=RNG)
svm = SVC(kernel="rbf", probability=True, random_state=RNG)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)

# -------------------------------
# 模型评估
# -------------------------------
def eval_model(clf, name):
    pred = clf.predict(X_test)
    proba = clf.predict_proba(X_test)[:,1]
    acc = accuracy_score(y_test, pred)
    auc = roc_auc_score(y_test, proba)
    fpr, tpr, _ = roc_curve(y_test, proba)
    return {"name":name, "pred":pred, "proba":proba, "acc":acc, "auc":auc, "fpr":fpr, "tpr":tpr}

res_lr  = eval_model(lr,  "LogisticRegression")
res_rf  = eval_model(rf,  "RandomForest")
res_svm = eval_model(svm, "SVM(RBF)")

# 保存指标文件
with open(os.path.join(OUTDIR, "metrics_task2.txt"), "w", encoding="utf-8") as f:
    for r in [res_lr, res_rf, res_svm]:
        f.write(f"{r['name']}: accuracy={r['acc']:.4f}, roc_auc={r['auc']:.4f}\n")

# 绘制ROC曲线 (单张图多条曲线)
plt.figure()
plt.plot(res_lr["fpr"], res_lr["tpr"], label=f"LR (AUC={res_lr['auc']:.2f})")
plt.plot(res_rf["fpr"], res_rf["tpr"], label=f"RF (AUC={res_rf['auc']:.2f})")
plt.plot(res_svm["fpr"], res_svm["tpr"], label=f"SVM (AUC={res_svm['auc']:.2f})")
plt.plot([0,1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "roc_curves.png"), dpi=160)
plt.close()

# 绘制混淆矩阵
def save_cm(clf, name, filename):
    pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, pred)
    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title(f"Confusion Matrix - {name}")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    for (i,j), val in np.ndenumerate(cm):
        plt.text(j, i, int(val), ha='center', va='center')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, filename), dpi=160)
    plt.close()

save_cm(lr,  "LogisticRegression", "confusion_matrix_logreg.png")
save_cm(rf,  "RandomForest",      "confusion_matrix_rf.png")
save_cm(svm, "SVM(RBF)",          "confusion_matrix_svm.png")

print("Task 2 completed.")