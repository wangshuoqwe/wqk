import whisper
import time
import os

# 加载模型
model = whisper.load_model("base")

# 音频路径（你导出的配音必须叫这个名字）
audio_path = "output.mp3"

if not os.path.exists(audio_path):
    print("请把剪映导出的音频改名为 output.mp3 并放在同一文件夹！")
    exit()

# 开始识别
start = time.time()
result = model.transcribe(audio_path, language="zh")
end = time.time()

print("=" * 50)
print("识别结果：")
print(result["text"])
print("=" * 50)
print(f"耗时：{end - start:.2f} 秒")

# 保存结果
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
