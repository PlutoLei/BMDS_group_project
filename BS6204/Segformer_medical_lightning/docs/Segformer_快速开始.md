# ⚡ 医学图像分割 - 5分钟快速开始

## 🎯 目标
快速验证环境配置，运行一个简短的训练示例。

---

## 步骤1️⃣: 安装依赖（5分钟）

### Windows用户

```bash
# 1. 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 2. 安装PyTorch (CUDA 11.8)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 3. 安装其他依赖
pip install transformers==4.35.0 lightning==2.1.0 albumentations==1.3.1
pip install torchmetrics==1.2.0 torchinfo==1.8.0 opencv-python==4.8.1.78
pip install matplotlib==3.8.0 wandb==0.16.0 requests
```

### Linux/Mac用户

```bash
# 1. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 2. 安装PyTorch
pip install torch torchvision

# 3. 安装其他依赖
pip install -r Segformer_requirements.txt
```

**验证安装**：
```python
import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
```

---

## 步骤2️⃣: 打开Notebook（1分钟）

1. 启动PyCharm
2. 打开文件: `Segformer_medical_lightning_PyCharm.ipynb`
3. 选择刚创建的虚拟环境作为kernel

---

## 步骤3️⃣: 快速测试（10分钟）

### 执行以下代码单元（按顺序）：

#### ✅ 第0-1部分：环境检查
```python
# 执行GPU检查和依赖导入
# 确保看到"✓ 所有依赖库已成功导入！"
```

#### ✅ 第2部分：配置参数
```python
# 直接运行，使用默认配置
```

#### ✅ 第3部分：准备数据
```python
# 首次运行会下载数据集（~500MB）
# 大约需要2-5分钟
```

#### ✅ 第7.4部分：快速训练
```python
# 找到这段代码并确保设置为True
QUICK_TEST = True  # ✓ 开启快速测试
TEST_EPOCHS = 5    # 只训练5个epoch

# 然后运行训练单元
# 预计时间：5-10分钟
```

---

## 步骤4️⃣: 查看结果（2分钟）

### 执行第8部分：推理和可视化
```python
# 加载训练好的模型
# 在验证集上查看分割效果
```

**期望输出**：
- 原始医学图像
- 真实分割标签（彩色掩码）
- 模型预测结果（彩色掩码）
- 叠加可视化

---

## 🎉 成功！

如果您看到了可视化结果，说明环境配置成功！

### 下一步：

1. **完整训练**：
   - 设置 `QUICK_TEST = False`
   - 训练100个epoch（3-8小时）
   - 获得更好的分割效果

2. **实验不同配置**：
   - 调整 `BATCH_SIZE`（根据GPU显存）
   - 尝试不同的 `MODEL_NAME`（b0-b5）
   - 修改学习率 `INIT_LR`

3. **启用WandB追踪**：
   - 注册 [wandb.ai](https://wandb.ai)
   - 设置 `USE_WANDB = True`
   - 实时监控训练过程

---

## ❓ 遇到问题？

### 问题1: CUDA out of memory

**解决**：减小批次大小
```python
TrainingConfig.BATCH_SIZE = 4  # 改为4或2
```

### 问题2: 数据下载失败

**解决**：手动下载
1. 访问 [Kaggle数据集](https://www.kaggle.com/datasets/learnopencvblog/uwm-gi-tract-segmentation-img-msk-split)
2. 下载并解压到 `dataset_UWM_GI_Tract_train_valid/`

### 问题3: 找不到GPU

**检查**：
```python
import torch
print(torch.cuda.is_available())  # 应该输出True
print(torch.cuda.get_device_name(0))  # 显示GPU名称
```

如果输出False：
- 确认已安装CUDA版本的PyTorch
- 检查NVIDIA驱动是否正常

---

## 📚 更多信息

- 详细使用说明: `Segformer_医学图像分割_使用说明.md`
- 完整Notebook: `Segformer_medical_lightning_PyCharm.ipynb`
- 依赖列表: `Segformer_requirements.txt`

---

## 🚀 快速命令汇总

```bash
# 安装
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
pip install -r Segformer_requirements.txt

# 验证
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# 启动
pycharm Segformer_medical_lightning_PyCharm.ipynb
```

---

**🎊 祝您使用愉快！**

预计总时间：**20-30分钟**
- 安装: 5分钟
- 配置: 1分钟
- 下载数据: 3分钟
- 快速训练: 10分钟
- 查看结果: 2分钟
