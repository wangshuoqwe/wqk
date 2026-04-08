import vosk
import pyaudio
import json
import os

def main():
    print("===== 任务3.2：Vosk 实时麦克风识别 =====")
    model_path = "vosk-model-small-cn-0.22"

    if not os.path.exists(model_path):
        print(f"错误：请将模型放在当前目录下，文件夹名：{model_path}")
        return

    # 加载模型
    print("正在加载 Vosk 中文模型...")
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

    print("\n实时识别已启动，请说话，按 Ctrl+C 停止\n")

    try:
        while True:
            data = stream.read(4096)
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print("识别结果：", res["text"])
    except KeyboardInterrupt:
        print("\n已停止实时识别")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
