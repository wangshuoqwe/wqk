import vosk
import pyaudio
import json
import os

def realtime_asr(model_dir="vosk-model-small-cn-0.22"):
    """
    任务三要求2：基于Vosk的实时麦克风识别
    :param model_dir: Vosk中文模型目录
    """
    print("="*50)
    print("任务三：基于Vosk的实时麦克风识别")
    print("按 Ctrl+C 停止识别")
    print("="*50)

    # 1. 加载模型
    if not os.path.exists(model_dir):
        print(f"错误：请下载Vosk模型并解压到目录 {model_dir}")
        print("下载地址：https://alphacephei.com/vosk/models")
        return

    model = vosk.Model(model_dir)
    rec = vosk.KaldiRecognizer(model, 16000)
    rec.SetWords(True)

    # 2. 打开麦克风流
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=4096
    )
    stream.start_stream()

    # 3. 实时识别循环
    try:
        while True:
            data = stream.read(4096)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print(f"\r实时识别: {res['text']}")
            # else:
            #     # 可选：显示部分结果
            #     partial = json.loads(rec.PartialResult())
            #     print(f"\r识别中: {partial['partial']}", end="")
    except KeyboardInterrupt:
        print("\n\n识别已手动停止")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    realtime_asr()
