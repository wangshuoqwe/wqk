import vosk
import pyaudio
import json
import os

# 模型路径（已经帮你固定好）
model_path = "vosk-model-small-cn-0.22"

if not os.path.exists(model_path):
    print("请把模型解压到当前文件夹！")
    print("文件夹名必须是：vosk-model-small-cn-0.22")
    exit()

# 加载模型
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)
rec.SetWords(True)

# 打开麦克风
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=4096
)

print("实时识别已开始，按 Ctrl+C 停止")

try:
    while True:
        data = stream.read(4096)
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print("识别：", res["text"])
except KeyboardInterrupt:
    print("\n识别结束")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
