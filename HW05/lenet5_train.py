import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm
import time

# ==================== 1. 超参数设置 ====================
BATCH_SIZE = 64
EPOCHS = 10
LEARNING_RATE = 0.001
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {DEVICE}")

# ==================== 2. 数据加载与预处理 ====================
transform = transforms.Compose([
    transforms.Resize((32, 32)),          # LeNet-5 原始的输入尺寸为 32x32
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
test_dataset = torchvision.datasets.MNIST(
    root='./data', train=False, download=True, transform=transform
)

train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=BATCH_SIZE, shuffle=True
)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=BATCH_SIZE, shuffle=False
)

# ==================== 3. LeNet-5 模型定义 ====================
class LeNet5(nn.Module):
    """
    经典的 LeNet-5 架构（基于 PyTorch 实现）
    输入尺寸：32x32x1（MNIST 图像被 Resize 到 32x32）
    """
    def __init__(self, num_classes=10):
        super(LeNet5, self).__init__()
        # C1: 卷积层，输入 1 通道，输出 6 通道，卷积核 5x5
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, stride=1, padding=0)
        # S2: 平均池化层（原始 LeNet-5 使用平均池化，此处也可改用最大池化）
        self.pool1 = nn.AvgPool2d(kernel_size=2, stride=2)
        # C3: 卷积层，输入 6 通道，输出 16 通道，卷积核 5x5
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0)
        # S4: 平均池化层
        self.pool2 = nn.AvgPool2d(kernel_size=2, stride=2)
        # C5: 卷积层（等价于全连接），输入 16 通道，输出 120 通道，卷积核 5x5
        self.conv3 = nn.Conv2d(16, 120, kernel_size=5, stride=1, padding=0)
        # F6: 全连接层，输出 84
        self.fc1 = nn.Linear(120, 84)
        # 输出层
        self.fc2 = nn.Linear(84, num_classes)

        self.relu = nn.ReLU()

    def forward(self, x):
        # 输入 32x32x1
        x = self.relu(self.conv1(x))      # -> 28x28x6
        x = self.pool1(x)                  # -> 14x14x6
        x = self.relu(self.conv2(x))      # -> 10x10x16
        x = self.pool2(x)                  # -> 5x5x16
        x = self.relu(self.conv3(x))      # -> 1x1x120
        # 展平
        x = x.view(x.size(0), -1)          # -> 120
        x = self.relu(self.fc1(x))         # -> 84
        x = self.fc2(x)                    # -> 10
        return x

model = LeNet5(num_classes=10).to(DEVICE)

# 打印模型结构和参数量
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"LeNet-5 可训练参数量: {count_parameters(model):,}")

# ==================== 4. 损失函数与优化器 ====================
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# ==================== 5. 训练循环 ====================
print("\n===== 开始训练 LeNet-5 =====")
start_time = time.time()

for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    loop = tqdm(train_loader, desc=f'Epoch {epoch+1}/{EPOCHS}')
    for images, labels in loop:
        images, labels = images.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        loop.set_postfix(loss=loss.item(), acc=100.0 * correct / total)

    epoch_loss = running_loss / len(train_loader)
    epoch_acc = 100.0 * correct / total
    print(f'Epoch {epoch+1} 训练 Loss: {epoch_loss:.4f}, 训练 Acc: {epoch_acc:.2f}%')

training_time = time.time() - start_time
print(f"\n训练总耗时: {training_time:.2f} 秒")

# ==================== 6. 测试评估 ====================
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(DEVICE), labels.to(DEVICE)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

test_acc = 100.0 * correct / total
print(f"\n===== LeNet-5 测试准确率: {test_acc:.2f}% =====")

# ==================== 7. 保存模型 ====================
torch.save(model.state_dict(), './models/lenet5.pth')
print("模型已保存至 ./models/lenet5.pth")
