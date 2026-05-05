import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from simple_cnn_train import SimpleCNN
from lenet5_train import LeNet5
import time

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_test_loader(batch_size=64, for_lenet=True):
    if for_lenet:
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
    else:
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
    test_dataset = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=transform
    )
    return torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

def evaluate_model(model, test_loader, model_name="Model"):
    model.eval()
    correct = 0
    total = 0
    start_time = time.time()
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    inference_time = time.time() - start_time
    acc = 100.0 * correct / total
    return acc, inference_time

# 评估极简 CNN
simple_model = SimpleCNN().to(DEVICE)
simple_model.load_state_dict(torch.load('./models/simple_cnn.pth', map_location=DEVICE))
simple_test_loader = load_test_loader(for_lenet=False)
simple_acc, simple_inf_time = evaluate_model(simple_model, simple_test_loader, "SimpleCNN")

# 评估 LeNet-5
lenet_model = LeNet5().to(DEVICE)
lenet_model.load_state_dict(torch.load('./models/lenet5.pth', map_location=DEVICE))
lenet_test_loader = load_test_loader(for_lenet=True)
lenet_acc, lenet_inf_time = evaluate_model(lenet_model, lenet_test_loader, "LeNet-5")

# 输出对比结果
print("\n" + "="*50)
print("模型对比结果")
print("="*50)
print(f"{'指标':<20} {'极简 CNN':<20} {'LeNet-5':<20}")
print("-"*60)
print(f"{'测试准确率':<20} {simple_acc:.2f}%{'':<15} {lenet_acc:.2f}%")
print(f"{'参数量':<20} ~62,000{'':<14} ~61,000")
print(f"{'单轮推理耗时':<20} {simple_inf_time:.4f}s{'':<12} {lenet_inf_time:.4f}s")
