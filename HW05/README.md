## 一.手写数字识别实验：极简 CNN 与 LeNet-5 对比

本项目为《计算机视觉》课程实验，基于 PyTorch 框架在 MNIST 数据集上实现并对比两种卷积神经网络：
- **极简 CNN**：一个简单的两层卷积 + 全连接网络（参考公众号文章）
- **LeNet-5**：经典的 LeNet-5 架构（适配 MNIST）

主要目标：
1. 理解 CNN 基本结构（卷积、池化、全连接）与训练流程
2. 实现 LeNet-5 并评估性能
3. 对比两种模型的准确率、参数量、推理时间等指标

---

## 二. 目录结构

mnist-cnn-lab/
├── README.md # 本文件
├── requirements.txt # 依赖包列表
├── debug_notes.md # 调试记录（任务一）
├── data/ # MNIST 数据（自动下载）
├── models/ # 保存训练好的模型权重
│ ├── simple_cnn.pth
│ └── lenet5.pth
├── simple_cnn_train.py # 极简 CNN 训练脚本
├── lenet5_train.py # LeNet-5 训练脚本
└── compare_models.py # 模型对比脚本

##  三.环境配置

## 1. 创建虚拟环境（推荐）
bash
conda create -n mnist-cnn python=3.9
conda activate mnist-cnn

或使用 venv：
python -m venv mnist-cnn-env
mnist-cnn-env\Scripts\activate      # Windows

## 2.安装依赖### 
pip install -r requirements.txt

## 3.验证环境
import torch
print(torch.__version__)
print("CUDA available:", torch.cuda.is_available())
