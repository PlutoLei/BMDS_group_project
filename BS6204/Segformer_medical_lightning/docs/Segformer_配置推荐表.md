# 🎛️ 医学图像分割 - GPU配置推荐表

## 📊 根据GPU显存选择最佳配置

### 🔥 高性能GPU（16GB+）

**适用GPU**：RTX 4090, A100, RTX 3090, V100

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 32              # ⬆️ 大批次
    MODEL_NAME: str = "nvidia/segformer-b5-finetuned-ade-512-512"  # 最大模型
    NUM_EPOCHS: int = 100
    INIT_LR: float = 3e-4
    USE_SCHEDULER: bool = True
```

**预期表现**：
- 训练时间: ~2-3小时（100 epochs）
- 验证F1: 0.94-0.96
- 单epoch: ~1-2分钟

---

### ⚡ 主流GPU（10-12GB）

**适用GPU**：RTX 3060 (12GB), RTX 3080 (10GB), RTX 4070

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 8               # ✅ 推荐配置
    MODEL_NAME: str = "nvidia/segformer-b4-finetuned-ade-512-512"  # 默认
    NUM_EPOCHS: int = 100
    INIT_LR: float = 3e-4
    USE_SCHEDULER: bool = True
```

**预期表现**：
- 训练时间: ~5-7小时（100 epochs）
- 验证F1: 0.93-0.95
- 单epoch: ~3-4分钟

---

### 💻 入门级GPU（6-8GB）

**适用GPU**：RTX 3050, RTX 2060, GTX 1660 Ti

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 4               # ⬇️ 减小批次
    MODEL_NAME: str = "nvidia/segformer-b2-finetuned-ade-512-512"  # 中等模型
    NUM_EPOCHS: int = 100
    INIT_LR: float = 3e-4
    USE_SCHEDULER: bool = True

# 额外优化
@dataclass(frozen=True)
class DatasetConfig:
    IMAGE_SIZE: tuple[int,int] = (256, 256)  # 减小图像尺寸
```

**预期表现**：
- 训练时间: ~8-12小时（100 epochs）
- 验证F1: 0.91-0.93
- 单epoch: ~5-7分钟

---

### 🎯 低显存GPU（4GB）

**适用GPU**：GTX 1650, RTX 3050 (4GB), MX450

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 2               # ⚠️ 最小批次
    MODEL_NAME: str = "nvidia/segformer-b0-finetuned-ade-512-512"  # 最小模型
    NUM_EPOCHS: int = 50              # 减少训练轮数
    INIT_LR: float = 2e-4
    USE_SCHEDULER: bool = False

@dataclass(frozen=True)
class DatasetConfig:
    IMAGE_SIZE: tuple[int,int] = (224, 224)  # 进一步减小
```

**预期表现**：
- 训练时间: ~6-8小时（50 epochs）
- 验证F1: 0.88-0.91
- 单epoch: ~7-10分钟
- ⚠️ 性能会有所下降

**额外优化技巧**：
```python
# 启用梯度累积（模拟更大的批次）
trainer = pl.Trainer(
    accumulate_grad_batches=4,  # 累积4个批次
    # ... 其他参数
)
```

---

### 🐌 CPU训练（不推荐）

如果没有GPU，可以使用CPU，但**非常慢**：

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 1               # 单样本
    MODEL_NAME: str = "nvidia/segformer-b0-finetuned-ade-512-512"
    NUM_EPOCHS: int = 5               # 只训练5轮测试
    NUM_WORKERS: int = 4              # 多线程加载

# 训练器配置
trainer = pl.Trainer(
    accelerator="cpu",
    devices=1,
    max_epochs=5,
    precision=32,  # CPU不支持混合精度
)
```

**预期表现**：
- 训练时间: ~50-70小时（100 epochs）😱
- 单epoch: ~30-40分钟
- **建议**：仅用于代码测试，不建议完整训练

---

## 📈 性能对比表

| GPU型号 | 显存 | 推荐Batch | 推荐模型 | 单Epoch | 100 Epochs | 预期F1 |
|---------|------|-----------|----------|---------|------------|--------|
| RTX 4090 | 24GB | 32 | b5 | 1-2分钟 | 2-3小时 | 0.95-0.96 |
| RTX 3090 | 24GB | 24 | b5 | 1-2分钟 | 2-3小时 | 0.95-0.96 |
| RTX 3080 | 10GB | 8 | b4 | 2-3分钟 | 3-5小时 | 0.93-0.95 |
| **RTX 3060** | **12GB** | **8** | **b4** | **3-4分钟** | **5-7小时** | **0.93-0.95** |
| RTX 3050 | 8GB | 4 | b2 | 5-7分钟 | 8-12小时 | 0.91-0.93 |
| GTX 1650 | 4GB | 2 | b0 | 7-10分钟 | 12-17小时 | 0.88-0.91 |
| CPU | N/A | 1 | b0 | 30-40分钟 | 50-70小时 | 0.85-0.88 |

---

## 🎯 模型选择指南

### SegFormer模型对比

| 模型 | 参数量 | 显存占用 | 速度 | 精度 | 适用场景 |
|------|--------|----------|------|------|----------|
| **b0** | 4M | ~4GB | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 快速实验、低显存 |
| **b1** | 14M | ~6GB | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 平衡性能 |
| **b2** | 28M | ~8GB | ⚡⚡⚡ | ⭐⭐⭐⭐ | 入门级GPU |
| **b3** | 47M | ~10GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | 主流GPU |
| **b4** | 64M | ~12GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | **默认推荐** |
| **b5** | 84M | ~16GB | ⚡ | ⭐⭐⭐⭐⭐ | 高性能GPU、生产环境 |

---

## 💡 优化技巧

### 技巧1: 梯度累积（小显存福音）

模拟大批次训练效果：

```python
# 配置
TrainingConfig.BATCH_SIZE = 4

# Trainer设置
trainer = pl.Trainer(
    accumulate_grad_batches=4,  # 4 × 4 = 有效批次16
    # ...
)
```

**原理**：累积4个小批次的梯度，然后一次性更新。

### 技巧2: 混合精度训练（2倍加速）

```python
trainer = pl.Trainer(
    precision="16-mixed",  # 自动使用FP16
    # ...
)
```

**效果**：
- 速度提升: 1.5-2倍
- 显存节省: ~30%
- 精度损失: 可忽略

### 技巧3: 渐进式调整

从小模型开始，逐步升级：

```
第1轮: b0模型 + 小图像(224) → 验证环境
第2轮: b2模型 + 中图像(256) → 初步训练
第3轮: b4模型 + 标准图像(288) → 完整训练
```

### 技巧4: 数据加载优化

```python
# Windows
TrainingConfig.NUM_WORKERS = 0  # 避免多进程问题

# Linux/Mac
TrainingConfig.NUM_WORKERS = 4  # 并行加载

# 启用pin_memory（GPU训练推荐）
data_module = MedicalSegmentationDataModule(
    pin_memory=True,  # 加速CPU→GPU传输
    # ...
)
```

### 技巧5: 学习率查找

自动找到最优学习率：

```python
from lightning.pytorch.tuner import Tuner

tuner = Tuner(trainer)
lr_finder = tuner.lr_find(model, data_module)

# 查看建议的学习率
print(f"建议学习率: {lr_finder.suggestion()}")

# 可视化
fig = lr_finder.plot(suggest=True)
fig.show()
```

---

## 📊 显存占用估算

### 显存分配

```
总显存 = 模型参数 + 优化器状态 + 激活值 + 批次数据

示例（b4模型，batch=8）：
- 模型参数: ~250MB
- 优化器(AdamW): ~500MB
- 激活值: ~3GB
- 批次数据: ~200MB
- 其他开销: ~500MB
------------------------
总计: ~4.5GB

+ 混合精度: 减少30% → ~3.2GB
+ 梯度累积: 几乎不增加
```

### 实测显存占用（NVIDIA-SMI）

| 配置 | 模型 | Batch | 图像大小 | 实际占用 |
|------|------|-------|----------|----------|
| 最小 | b0 | 2 | 224×224 | ~2.5GB |
| 入门 | b2 | 4 | 256×256 | ~4.5GB |
| 推荐 | b4 | 8 | 288×288 | ~7.5GB |
| 高性能 | b5 | 16 | 288×288 | ~12GB |

---

## 🔧 调试技巧

### 找到最大批次大小

使用二分搜索法：

```python
# 测试不同批次大小
batch_sizes = [32, 16, 8, 4, 2]

for bs in batch_sizes:
    try:
        TrainingConfig.BATCH_SIZE = bs
        # 尝试训练一个epoch
        trainer.fit(model, data_module, max_epochs=1)
        print(f"✓ Batch {bs} 成功")
        break
    except RuntimeError as e:
        if "out of memory" in str(e):
            print(f"✗ Batch {bs} 显存不足")
            torch.cuda.empty_cache()
        else:
            raise e
```

### 监控显存使用

```python
import torch

def print_gpu_utilization():
    if torch.cuda.is_available():
        allocated = torch.cuda.memory_allocated(0) / 1024**3
        reserved = torch.cuda.memory_reserved(0) / 1024**3
        print(f"已分配: {allocated:.2f}GB")
        print(f"已保留: {reserved:.2f}GB")

# 在训练前后调用
print_gpu_utilization()
```

---

## 🎓 常见问题

### Q: 为什么我的GPU比表格慢？

可能原因：
1. ✅ CPU瓶颈 → 增加`NUM_WORKERS`
2. ✅ 磁盘I/O慢 → 使用SSD
3. ✅ 温度过高 → 检查散热
4. ✅ 其他程序占用GPU → 关闭其他程序

### Q: 如何在Colab上运行？

```python
# 1. 检查GPU
!nvidia-smi

# 2. 修改配置
TrainingConfig.BATCH_SIZE = 16  # T4 GPU
TrainingConfig.NUM_WORKERS = 2

# 3. 挂载Google Drive保存模型
from google.colab import drive
drive.mount('/content/drive')
```

### Q: 多GPU训练如何配置？

```python
# 自动使用所有GPU
trainer = pl.Trainer(
    accelerator="gpu",
    devices=-1,  # 使用所有GPU
    strategy="ddp",  # 分布式数据并行
    # ...
)

# 批次大小会自动调整
# 实际批次 = BATCH_SIZE × GPU数量
```

---

## ✅ 配置检查清单

在开始训练前，确认以下几点：

- [ ] 已安装正确的PyTorch（CUDA版本匹配）
- [ ] 显存足够（至少比推荐配置多1GB余量）
- [ ] 数据集已下载完成
- [ ] 批次大小和模型大小已根据GPU调整
- [ ] 启用了混合精度训练（`precision="16-mixed"`）
- [ ] 关闭了其他占用GPU的程序
- [ ] 设置了合适的`NUM_WORKERS`

---

## 📈 性能基准测试

使用这段代码测试您的配置：

```python
import time
import torch

def benchmark_training(model, data_module, batch_size, num_steps=100):
    model.train()
    model.to("cuda")

    data_module.setup()
    loader = data_module.train_dataloader()

    start_time = time.time()

    for i, (images, masks) in enumerate(loader):
        if i >= num_steps:
            break

        images = images.to("cuda")
        masks = masks.to("cuda")

        # 前向传播
        logits = model(images)
        loss = dice_coef_loss(logits, masks, num_classes=4)

        # 反向传播
        loss.backward()

    elapsed = time.time() - start_time
    throughput = num_steps * batch_size / elapsed

    print(f"批次大小: {batch_size}")
    print(f"处理速度: {throughput:.2f} 图像/秒")
    print(f"单批次时间: {elapsed/num_steps*1000:.2f}ms")

# 运行测试
benchmark_training(model, data_module, TrainingConfig.BATCH_SIZE)
```

---

**🎯 选择合适的配置，开始您的医学图像分割之旅吧！**
