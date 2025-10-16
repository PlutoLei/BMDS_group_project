# 🚀 训练启动指南（解决OOM问题）

## ⚠️ 当前问题
CUDA内存溢出 - 有旧的Python进程占用GPU内存

---

## 📋 启动前检查清单

### ✅ 步骤1：清理GPU进程（必须！）

**方法A：使用批处理脚本（推荐）**
```bash
# 在VSCode_Project目录下运行
kill_gpu_process.bat
```

**方法B：手动杀死进程**
```bash
# 查看进程
tasklist | findstr python.exe

# 杀死所有Python进程
taskkill /F /IM python.exe /T
```

**方法C：重启电脑**（如果上面都不行）

---

### ✅ 步骤2：验证GPU已清空

运行此命令，确保内存使用 < 500MB：
```bash
nvidia-smi
```

期望输出：
```
Memory-Usage: 100MB / 8188MB  ✓ (清空了)
```

---

### ✅ 步骤3：在Jupyter中操作

#### 3.1 重启Kernel（关键！）
```
点击 Kernel → Restart Kernel
```
或快捷键 `Ctrl + .` 选择 Restart

#### 3.2 逐步运行Cell
**不要使用 Run All！** 按顺序运行：

1. ✓ 导入库
2. ✓ 配置环境（包含PYTORCH_CUDA_ALLOC_CONF）
3. ✓ 定义数据集类
4. ✓ 定义模型
5. ✓ 定义训练配置
6. ⚠️ **在训练前**，验证GPU清空：
   ```python
   import torch
   print(f"GPU内存: {torch.cuda.memory_allocated()/1024**3:.2f}GB")
   # 应该显示 0.00GB 或接近0
   ```
7. ✓ 开始训练

---

## 🎯 当前优化配置

已完成以下**极限优化**：

```python
# 模型配置
MODEL_NAME = "nvidia/segformer-b0-finetuned-ade-512-512"  # 最小模型
BATCH_SIZE = 2                                            # 极小批次
IMAGE_SIZE = (288, 288)                                   # 中等图像尺寸

# Trainer配置
precision = "16-mixed"           # FP16混合精度（节省50%内存）
accumulate_grad_batches = 4      # 梯度累积（有效批次=8）

# 环境变量
PYTORCH_CUDA_ALLOC_CONF = "expandable_segments:True"  # 减少碎片化
```

---

## 📊 预期内存占用

| 组件 | 内存占用 |
|------|---------|
| Segformer-B0 模型 | ~1.0GB |
| 批次数据 (2×288×288) | ~0.3GB |
| 优化器状态 | ~1.0GB |
| 前向+反向传播 | ~1.5GB |
| PyTorch开销 | ~0.5GB |
| **总计** | **~4-5GB / 8GB** ✓ |

**安全余量**：3GB（足够）

---

## 🔍 训练过程中的监控

### 实时监控GPU（另开命令行）
```bash
nvidia-smi -l 1
```

### 期望值
- **空闲时**：<500MB
- **训练时**：4-5GB
- **峰值**：<6GB

如果超过6GB，立即停止训练（Ctrl+C）

---

## ⚠️ 如果仍然OOM

### 选项1：进一步降低批次大小
修改notebook中的配置：
```python
class TrainingConfig:
    BATCH_SIZE: int = 1  # 改为1
```

然后修改Trainer：
```python
accumulate_grad_batches=8,  # 改为8，保持有效批次=8
```

### 选项2：减小图像尺寸
```python
class DatasetConfig:
    IMAGE_SIZE: Tuple[int, int] = (224, 224)  # 改为224
```

### 选项3：关闭数据增强（训练时）
临时测试用，在MedicalDataset中设置：
```python
is_train=False  # 关闭增强
```

---

## ✅ 训练成功标志

看到这些输出说明成功：
```
✓ GPU缓存已清理
  当前GPU内存占用: 0.00GB
  GPU设备: NVIDIA GeForce RTX 4060 Laptop GPU

Epoch 0:   0%|          | 0/500 [00:00<?, ?it/s]
```

---

## 🎓 模型性能对比

| 模型 | 参数 | 内存 | 相对性能 |
|------|-----|------|---------|
| B0 (当前) | 3.7M | ~4GB | 100% (基准) |
| B1 | 14M | ~5GB | +3-5% |
| B2 | 28M | ~6GB | +5-8% |
| B4 | 64M | ~8GB+ | +8-12% |

**B0是8GB GPU的最佳选择！**

---

## 📞 故障排除

### Q: 还是显示13.54GB占用？
A: **Kernel没有重启**，必须重启Jupyter Kernel

### Q: 训练很慢？
A: 正常，梯度累积会稍微降低速度，但保证能训练

### Q: 想用更大的模型？
A: 考虑：
   - 升级GPU到16GB+
   - 使用Google Colab（免费T4 16GB）
   - 租用云GPU

---

## 🚀 开始训练

**完整流程（按顺序）：**

1. ✓ 运行 `kill_gpu_process.bat`
2. ✓ 检查 `nvidia-smi`（确认<500MB）
3. ✓ 打开Jupyter Notebook
4. ✓ Kernel → Restart Kernel
5. ✓ 逐个运行Cell
6. ✓ 开始训练！

**祝训练顺利！** 🎉

---

*最后更新：2025-10-12*
*配置：Segformer-B0 + Batch=2 + Grad_Accum=4 + FP16*
