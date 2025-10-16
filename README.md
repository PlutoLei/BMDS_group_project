# BS6204 Medical Image Segmentation Project

<div align="center">

**基于 SegFormer 的医学图像语义分割项目**

*Medical Image Semantic Segmentation Using SegFormer Transformer*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![Lightning](https://img.shields.io/badge/Lightning-2.1+-792ee5.svg)](https://lightning.ai/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📖 项目简介 | Project Overview

本项目使用 NVIDIA 的 **SegFormer** transformer 模型对医学图像（胃肠道 CT 扫描）进行语义分割，实现对**胃部、小肠、大肠**三个器官的自动识别和分割。

This project uses NVIDIA's **SegFormer** transformer model for semantic segmentation of medical images (gastrointestinal CT scans), achieving automatic recognition and segmentation of three organs: **stomach, small intestine, and large intestine**.

### 🎯 主要特性 | Key Features

- 🔥 **先进架构**: 基于 Vision Transformer 的 SegFormer 模型
- ⚡ **高性能训练**: 使用 PyTorch Lightning 框架，支持混合精度训练
- 📊 **实验追踪**: 集成 Weights & Biases 实时监控训练过程
- 🖼️ **数据增强**: 使用 Albumentations 进行医学图像增强
- 📈 **高精度**: 验证集 F1-Score 达到 0.93-0.95

---

## 🚀 快速开始 | Quick Start

### 环境要求 | Requirements

- **GPU**: NVIDIA GPU with 8GB+ VRAM (推荐 RTX 3060 或更高)
- **Python**: 3.8+
- **CUDA**: 11.0+

### 安装依赖 | Installation

```bash
# 克隆项目
git clone https://github.com/PlutoLei/BMDS_group_project.git
cd BMDS_group_project

# 安装 PyTorch (CUDA 11.8)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 安装其他依赖
pip install transformers==4.35.0 lightning==2.1.0 albumentations==1.3.1
pip install torchmetrics==1.2.0 wandb==0.16.0 opencv-python matplotlib
```

### 运行训练 | Run Training

```bash
# 打开 Jupyter Notebook
jupyter notebook BS6204/Segformer_medical_lightning/Segformer_medical_lightning.ipynb

# 按顺序执行每个单元格
# 数据集会自动下载 (~500MB)
```

---

## 📂 项目结构 | Project Structure

```
BS6204/
└── Segformer_medical_lightning/
    ├── Segformer_medical_lightning.ipynb  # 主训练 Notebook
    └── docs/                               # 项目文档
        ├── START_TRAINING.md              # 快速开始指南
        ├── Segformer_医学图像分割_使用说明.md  # 完整使用说明
        ├── Segformer_快速开始.md            # 快速入门
        ├── Segformer_配置推荐表.md          # 配置推荐
        ├── 训练优化改善报告_20251014.md     # 训练优化报告
        ├── 项目优化完整总结_20251014.md     # 项目优化总结
        └── 项目总结.md                      # 项目总结
```

---

## 🛠️ 技术栈 | Tech Stack

- **深度学习框架**: PyTorch 2.0+ & PyTorch Lightning 2.1+
- **模型**: SegFormer (NVIDIA) - Vision Transformer
- **数据增强**: Albumentations
- **实验追踪**: Weights & Biases (WandB)
- **评估指标**: TorchMetrics (Dice F1-Score)
- **可视化**: Matplotlib, OpenCV

---

## 📊 性能指标 | Performance Metrics

| 指标 Metric | 训练集 Train | 验证集 Validation |
|-------------|-------------|------------------|
| Loss | 0.25-0.30 | 0.30-0.35 |
| F1-Score (Dice) | 0.95-0.97 | **0.93-0.95** |

### 各类别性能 | Per-Class Performance

| 类别 Class | F1-Score | 难度 Difficulty |
|-----------|----------|----------------|
| 背景 Background | ~0.98 | 简单 Easy |
| 胃部 Stomach | ~0.92-0.94 | 中等 Medium |
| 小肠 Small Intestine | ~0.88-0.92 | 困难 Hard |
| 大肠 Large Intestine | ~0.90-0.93 | 中等 Medium |

---

## 📚 文档导航 | Documentation

详细文档请查看 `docs/` 目录：

1. **[快速开始](BS6204/Segformer_medical_lightning/docs/START_TRAINING.md)** - 5分钟快速上手
2. **[完整使用说明](BS6204/Segformer_medical_lightning/docs/Segformer_医学图像分割_使用说明.md)** - 详细配置和使用指南
3. **[配置推荐表](BS6204/Segformer_medical_lightning/docs/Segformer_配置推荐表.md)** - 不同 GPU 的配置建议
4. **[训练优化报告](BS6204/Segformer_medical_lightning/docs/训练优化改善报告_20251014.md)** - 训练优化细节
5. **[项目总结](BS6204/Segformer_medical_lightning/docs/项目总结.md)** - 项目完整总结

---

## 🎓 数据集 | Dataset

**UW-Madison GI Tract Image Segmentation**

- **来源**: [Kaggle Competition](https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation)
- **大小**: ~500MB
- **类别**: 4类 (背景, 胃, 小肠, 大肠)
- **训练集**: 3,600+ 图像
- **验证集**: 900+ 图像
- **图像尺寸**: 288×288 (预处理后)

---

## ⚙️ 支持的模型 | Supported Models

| 模型 Model | 参数量 Params | 显存需求 VRAM | 推荐用途 Use Case |
|-----------|--------------|--------------|----------------|
| segformer-b0 | 4M | ~4GB | 快速实验 Quick Test |
| segformer-b1 | 14M | ~6GB | 平衡性能 Balanced |
| segformer-b2 | 28M | ~8GB | 高精度 High Accuracy |
| segformer-b3 | 47M | ~10GB | 生产环境 Production |
| **segformer-b4** | **64M** | **~12GB** | **默认 Default** |
| segformer-b5 | 84M | ~16GB | 最高精度 Best |

---

## 🔬 主要功能 | Main Features

### 1. 自动数据下载和预处理
- 自动从 Kaggle 下载数据集
- 智能数据增强（旋转、翻转、亮度调整等）
- 自动划分训练集和验证集

### 2. 端到端训练流程
- 配置化超参数管理
- 自动保存最佳模型
- 实时训练监控和可视化

### 3. 模型评估和推理
- 多种评估指标（Dice F1、IoU）
- 可视化分割结果
- 支持批量推理

### 4. 实验追踪
- WandB 云端实验管理
- TensorBoard 本地可视化
- 训练曲线自动保存

---

## ⚠️ 注意事项 | Important Notes

1. **医疗用途声明**: 本模型仅用于教育和研究目的，不应直接用于临床诊断
2. **数据隐私**: 使用私有医学数据时请遵守相关法规（HIPAA 等）
3. **硬件要求**: 建议使用 GPU 训练，CPU 训练速度极慢（50-70小时）
4. **版本兼容**: Python 3.8-3.10，PyTorch 2.0+

---

## 🤝 参考文献 | References

### 论文 Papers

1. **SegFormer**: [Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203)
2. **Vision Transformer**: [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)
3. **Dice Loss**: [V-Net: Fully Convolutional Neural Networks](https://arxiv.org/abs/1606.04797)

### 资源 Resources

- [PyTorch Lightning 文档](https://lightning.ai/docs/pytorch/stable/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [SegFormer 官方实现](https://github.com/NVlabs/SegFormer)

---

## 📄 许可证 | License

本项目基于 MIT 许可证开源。

**引用 Citation**:
```bibtex
@article{xie2021segformer,
  title={SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers},
  author={Xie, Enze and Wang, Wenhai and Yu, Zhiding and Anandkumar, Anima and Alvarez, Jose M and Luo, Ping},
  journal={NeurIPS},
  year={2021}
}
```

---

## 🌟 致谢 | Acknowledgments

- 原始数据集提供: [UW-Madison Carbone Cancer Center](https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation)
- SegFormer 模型: [NVIDIA Research](https://github.com/NVlabs/SegFormer)
- 参考教程: [LearnOpenCV](https://learnopencv.com)

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给一个 Star！**

**If this project helps you, please give it a Star!**

</div>
