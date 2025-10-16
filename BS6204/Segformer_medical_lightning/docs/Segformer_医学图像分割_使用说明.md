# 医学图像分割项目使用指南 (PyCharm版)

## 📋 项目简介

本项目使用NVIDIA的SegFormer transformer模型对医学图像（胃肠道CT扫描）进行语义分割，实现对胃部、小肠、大肠三个器官的自动识别和分割。

**技术栈**:
- 🔥 PyTorch & PyTorch Lightning
- 🤗 HuggingFace Transformers
- 📊 Weights & Biases (实验追踪)
- 🖼️ Albumentations (数据增强)
- 📈 TorchMetrics (评估指标)

---

## 🚀 快速开始

### 1. 环境要求

**硬件要求**:
- GPU: 至少8GB显存 (推荐: NVIDIA RTX 3060或更高)
- RAM: 16GB以上
- 存储: 10GB可用空间

**软件要求**:
- Python 3.8+
- CUDA 11.0+ (GPU训练)
- PyCharm Professional 或 PyCharm Community + Jupyter插件

### 2. 安装依赖

#### 方法1: 使用pip（推荐）

```bash
# 创建虚拟环境（可选但推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装PyTorch (根据您的CUDA版本选择)
# CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# CPU版本（不推荐用于训练）
pip install torch torchvision

# 安装其他依赖
pip install transformers==4.35.0
pip install lightning==2.1.0
pip install albumentations==1.3.1
pip install torchmetrics==1.2.0
pip install torchinfo==1.8.0
pip install opencv-python==4.8.1.78
pip install matplotlib==3.8.0
pip install wandb==0.16.0
pip install requests
```

#### 方法2: 使用requirements.txt

创建`requirements.txt`文件并运行：

```bash
pip install -r requirements.txt
```

### 3. 配置PyCharm

#### 3.1 打开项目

1. 启动PyCharm
2. File → Open → 选择项目文件夹
3. 等待索引完成

#### 3.2 配置Python解释器

1. File → Settings → Project → Python Interpreter
2. 点击齿轮图标 → Add
3. 选择现有的虚拟环境或创建新环境
4. 应用更改

#### 3.3 配置Jupyter

1. File → Settings → Languages & Frameworks → Jupyter
2. 确保"Jupyter Server"已启动
3. 推荐设置：
   - 启用"Run cells with Shift-Enter"
   - 启用"Auto-scroll cell output"

### 4. 运行Notebook

1. 打开`Segformer_medical_lightning_PyCharm.ipynb`
2. 按顺序执行每个单元格（Shift + Enter）
3. 首次运行会自动下载：
   - 数据集 (~500MB)
   - 预训练模型权重 (~250MB)

---

## 📊 项目结构

```
VSCode_Project/
├── Segformer_medical_lightning_PyCharm.ipynb  # 主Notebook
├── 深度学习_基于Python的理论与实现/
│   ├── 10_逻辑回归与激活函数实践_PyCharm版.ipynb
│   └── 学习笔记/
│       └── 逻辑回归与激活函数详解.md
├── dataset_UWM_GI_Tract_train_valid/        # 数据集（自动下载）
│   ├── train/
│   │   ├── images/
│   │   └── masks/
│   └── valid/
│       ├── images/
│       └── masks/
└── lightning_logs/                            # 训练日志
    └── checkpoints/                           # 模型检查点
```

---

## ⚙️ 配置说明

### 数据集配置

在notebook的"2. 超参数配置"部分：

```python
@dataclass(frozen=True)
class DatasetConfig:
    NUM_CLASSES: int = 4          # 类别数（含背景）
    IMAGE_SIZE: (288, 288)        # 图像大小
    MEAN: (0.485, 0.456, 0.406)   # ImageNet归一化均值
    STD: (0.229, 0.224, 0.225)    # ImageNet归一化标准差
```

### 训练配置

```python
@dataclass
class TrainingConfig:
    BATCH_SIZE: int = 8           # 批次大小（根据显存调整）
    NUM_EPOCHS: int = 100         # 训练轮数
    INIT_LR: float = 3e-4         # 初始学习率
    OPTIMIZER_NAME: str = "AdamW" # 优化器
    USE_SCHEDULER: bool = True    # 是否使用学习率调度器
```

**批次大小建议**:
- RTX 3060 (12GB): BATCH_SIZE = 8
- RTX 3080 (10GB): BATCH_SIZE = 6-8
- RTX 4090 (24GB): BATCH_SIZE = 16-32
- 如果遇到显存不足 (OOM)，减小BATCH_SIZE

### 模型配置

支持的SegFormer模型（从小到大）：

| 模型 | 参数量 | 显存需求 | 推荐场景 |
|------|--------|----------|----------|
| segformer-b0 | 4M | ~4GB | 快速实验 |
| segformer-b1 | 14M | ~6GB | 平衡性能 |
| segformer-b2 | 28M | ~8GB | 高精度 |
| segformer-b3 | 47M | ~10GB | 生产环境 |
| **segformer-b4** | **64M** | **~12GB** | **本项目默认** |
| segformer-b5 | 84M | ~16GB | 最高精度 |

修改模型：
```python
MODEL_NAME: str = "nvidia/segformer-b0-finetuned-ade-512-512"  # 更小的模型
```

---

## 🎯 使用流程

### 阶段1: 环境测试（5-10分钟）

1. **执行前4个部分**:
   - 0. GPU检查
   - 1. 环境配置与依赖检查
   - 2. 超参数配置
   - 3. 数据集加载（会自动下载）

2. **设置快速测试模式**:
   ```python
   QUICK_TEST = True
   TEST_EPOCHS = 5  # 只训练5个epoch
   ```

3. **运行快速训练**（第7部分）
   - 验证环境配置正确
   - 熟悉训练流程
   - 预计时间: 10-20分钟

### 阶段2: 完整训练（数小时）

1. **关闭快速测试**:
   ```python
   QUICK_TEST = False
   ```

2. **可选：启用WandB追踪**:
   ```python
   USE_WANDB = True
   ```
   - 需要先注册 [wandb.ai](https://wandb.ai)
   - 首次运行会要求输入API key

3. **开始完整训练**
   - 100 epochs预计时间: 3-8小时（取决于GPU）
   - 模型会自动保存在`lightning_logs/`

### 阶段3: 模型推理

1. **加载最佳模型**（第8.1部分）
2. **评估验证集**（第8.2部分）
3. **可视化结果**（第8.3部分）

---

## 📈 监控训练

### 方法1: PyCharm内置监控

训练过程中会在进度条显示：
```
Epoch 50/100: 100%|████| 450/450 [02:15<00:00, 3.31it/s,
  train/batch_loss=0.315, train/batch_f1=0.932, v_num=0]
```

### 方法2: TensorBoard（默认）

```bash
# 在终端运行
tensorboard --logdir lightning_logs/

# 打开浏览器访问
http://localhost:6006
```

### 方法3: Weights & Biases（推荐）

启用后可实时查看：
- 训练/验证损失曲线
- F1分数趋势
- 学习率变化
- 系统资源使用
- 预测结果可视化

---

## 🔧 常见问题

### Q1: CUDA out of memory错误

**原因**: 显存不足

**解决方法**:
1. 减小`BATCH_SIZE`（从8改为4或2）
2. 使用更小的模型（b0或b1）
3. 减小图像尺寸（不推荐）

```python
TrainingConfig.BATCH_SIZE = 4  # 减半
```

### Q2: 数据集下载失败

**解决方法**:
1. 检查网络连接
2. 手动下载数据集：
   - [Kaggle链接](https://www.kaggle.com/datasets/learnopencvblog/uwm-gi-tract-segmentation-img-msk-split)
3. 解压到`dataset_UWM_GI_Tract_train_valid/`

### Q3: 训练速度慢

**可能原因**:
1. 使用CPU训练（非常慢）
2. `NUM_WORKERS`设置不当
3. 磁盘I/O瓶颈

**解决方法**:
```python
# Windows系统
TrainingConfig.NUM_WORKERS = 0

# Linux/Mac系统
TrainingConfig.NUM_WORKERS = 4
```

### Q4: PyCharm Jupyter无法连接

**解决方法**:
1. File → Settings → Tools → Python Scientific
2. 取消勾选"Show plots in tool window"
3. 重启PyCharm

### Q5: 模型加载警告

```
Some weights were not initialized from the model checkpoint...
You should probably TRAIN this model...
```

**说明**: 这是正常的！因为我们改变了输出类别数（从150改为4），分类头会被重新初始化。

### Q6: 中文字体显示问题

Matplotlib中文显示为方框，修改notebook中的字体配置：

```python
# Windows
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# Mac
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# Linux
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
```

---

## 📊 预期结果

### 训练指标

经过100个epoch的训练，预期达到：

| 指标 | 训练集 | 验证集 |
|------|--------|--------|
| Loss | 0.25-0.30 | 0.30-0.35 |
| F1-Score (Dice) | 0.95-0.97 | 0.93-0.95 |

### 各类别性能

| 类别 | F1-Score | 难度 |
|------|----------|------|
| 背景 | ~0.98 | 简单 |
| 胃部 | ~0.92-0.94 | 中等 |
| 小肠 | ~0.88-0.92 | 困难 |
| 大肠 | ~0.90-0.93 | 中等 |

### 训练时间参考

| GPU | 单个Epoch | 100 Epochs | 推理速度 |
|-----|-----------|------------|----------|
| RTX 3060 | ~3-4分钟 | 5-7小时 | ~30ms/张 |
| RTX 3080 | ~2-3分钟 | 3-5小时 | ~20ms/张 |
| RTX 4090 | ~1-2分钟 | 2-3小时 | ~15ms/张 |
| CPU | ~30-40分钟 | 50-70小时 | ~500ms/张 |

---

## 🎓 学习资源

### 必读论文

1. **SegFormer**: [Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203)
2. **Vision Transformer**: [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)
3. **Dice Loss**: [V-Net: Fully Convolutional Neural Networks](https://arxiv.org/abs/1606.04797)

### 推荐教程

1. [PyTorch Lightning官方文档](https://lightning.ai/docs/pytorch/stable/)
2. [HuggingFace Transformers教程](https://huggingface.co/docs/transformers)
3. [医学图像分割综述](https://arxiv.org/abs/2009.13120)

### 相关项目

1. [Kaggle竞赛页面](https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation)
2. [SegFormer官方实现](https://github.com/NVlabs/SegFormer)
3. [医学分割benchmark](https://medicalsegmentation.com/)

---

## 🔬 进阶实验

### 实验1: 数据增强对比

```python
# 关闭数据增强
# 在MedicalDataset类中设置
is_train=False  # 即使是训练集

# 对比F1分数差异
```

### 实验2: 不同模型对比

```python
# 测试不同大小的SegFormer
models = [
    "nvidia/segformer-b0-finetuned-ade-512-512",
    "nvidia/segformer-b2-finetuned-ade-512-512",
    "nvidia/segformer-b4-finetuned-ade-512-512",
]
```

### 实验3: 损失函数消融实验

```python
# 只使用Dice Loss
def dice_loss_only(predictions, ground_truths, num_classes=4):
    # ... (只计算Dice，不加CE)
    return 1.0 - dice_mean

# 只使用Cross Entropy
criterion = nn.CrossEntropyLoss()
```

### 实验4: 学习率调优

```python
# 使用学习率查找器
from lightning.pytorch.tuner import Tuner

tuner = Tuner(trainer)
lr_finder = tuner.lr_find(model, data_module)
lr_finder.plot()
```

---

## 📝 项目扩展

### 扩展1: 导出ONNX模型

```python
# 在推理部分添加
dummy_input = torch.randn(1, 3, 288, 288).to(DEVICE)
torch.onnx.export(
    model.model,
    dummy_input,
    "segformer_medical.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}}
)
```

### 扩展2: 创建Gradio应用

```python
import gradio as gr

def predict_image(image):
    # 预处理
    # 推理
    # 后处理
    return overlayed_image

demo = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(),
    outputs=gr.Image(),
    title="医学图像分割"
)
demo.launch()
```

### 扩展3: 批量推理脚本

创建`batch_inference.py`：

```python
import torch
from pathlib import Path

def batch_inference(model, image_folder, output_folder):
    image_paths = Path(image_folder).glob("*.png")
    for img_path in image_paths:
        # 加载图像
        # 推理
        # 保存结果
        pass
```

---

## ⚠️ 注意事项

1. **数据隐私**: 本项目使用公开数据集，如使用私有医学数据请遵守相关法规（HIPAA等）

2. **医疗用途**: 本模型仅用于教育和研究目的，不应直接用于临床诊断

3. **性能优化**:
   - 首次运行会编译CUDA kernels，可能较慢
   - 使用SSD存储数据集以提高I/O速度
   - 关闭其他GPU程序以释放显存

4. **版本兼容**:
   - PyTorch >= 2.0推荐
   - Python 3.11+可能有兼容性问题，建议3.8-3.10

---

## 🤝 贡献与反馈

如果您在使用过程中遇到问题或有改进建议：

1. 检查本文档的"常见问题"部分
2. 查看notebook中的详细注释
3. 参考官方文档链接

---

## 📄 许可证

本项目基于MIT许可证开源。

**引用**:
```bibtex
@article{xie2021segformer,
  title={SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers},
  author={Xie, Enze and Wang, Wenhai and Yu, Zhiding and Anandkumar, Anima and Alvarez, Jose M and Luo, Ping},
  journal={NeurIPS},
  year={2021}
}
```

---

## 📞 联系方式

- 原始教程: [LearnOpenCV](https://learnopencv.com)
- PyCharm优化版: 2025年10月

---

**✓ 祝您使用愉快，训练顺利！**

如有任何问题，请参考notebook中的详细注释或查阅相关文档。
