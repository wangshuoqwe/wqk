# 肺炎X光图像检测（基于ResNet50迁移学习）

本项目使用深度学习技术，基于胸部X光图像自动检测肺炎（Pneumonia）。模型采用迁移学习策略，以预训练的ResNet50作为特征提取基础，在公开的胸部X光数据集上微调，实现二分类（正常 / 肺炎）。

## 项目特点

- 使用 **ResNet50**（ImageNet预训练权重）作为骨干网络
- 自定义顶层：全局平均池化 + Dropout + 全连接层
- 数据增强：旋转、缩放、水平翻转、剪切变换等，提高泛化能力
- 训练/验证集按 **8:2** 自动划分（来自原始训练集）
- 独立的测试集评估，输出完整分类报告和混淆矩阵
- 自动生成训练曲线（损失、准确率）及混淆矩阵图

## 数据集结构

项目假设数据集位于 `./chest_xray/` 目录下，包含以下标准结构：
chest_xray/
├── train/
│ ├── NORMAL/
│ │ └── (正常X光图像)
│ └── PNEUMONIA/
│ └── (肺炎X光图像)
└── test/
├── NORMAL/
│ └── (正常X光图像)
└── PNEUMONIA/
└── (肺炎X光图像)

> 如果使用 [Kaggle Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) 数据集，解压后重命名主文件夹为 `chest_xray` 即可。

## 环境依赖

- Python 3.7+
- TensorFlow 2.x
- scikit-learn
- matplotlib
- seaborn
- numpy

安装所有依赖：

```bash
pip install tensorflow scikit-learn matplotlib seaborn numpy
