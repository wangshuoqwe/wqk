import vosk
import pyaudio
import json
import os

def main():
    """
    任务3：基于Vosk的实时麦克风语音识别
    功能：打开麦克风，实时将语音转写为文字
    """
    print("=" * 60)
    print("任务3：Vosk 实时麦克风语音识别")
    print("按 Ctrl+C 可停止识别")
    print("=" * 60)

    # -------------------------- 1. 配置参数 --------------------------
    # Vosk中文轻量模型路径（需下载解压到hw04目录，文件夹名不可修改）
    model_dir = "vosk-model-small-cn-0.22"

    # -------------------------- 2. 检查模型 --------------------------
    if not os.path.exists(model_dir):
        print(f"错误：未找到Vosk模型目录 {model_dir}")
        print("请下载模型并解压到hw04目录，下载地址：https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip")
        return

    # -------------------------- 3. 加载模型 --------------------------
    print("正在加载Vosk中文模型...")
    model = vosk.Model(model_dir)
    # 初始化识别器，采样率16000（Vosk要求）
    recognizer = vosk.KaldiRecognizer(model, 16000)
    # 开启单词级识别（可选，提升识别精度）
    recognizer.SetWords(True)
    print("模型加载完成！")

    # -------------------------- 4. 初始化麦克风 --------------------------
    p = pyaudio.PyAudio()
    # 配置麦克风流：16位单声道，16000采样率，缓冲区4096
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=4096
    )
    stream.start_stream()
    print("\n实时识别已启动，请对着麦克风说话...\n")

    # -------------------------- 5. 实时识别循环 --------------------------
    try:
        while True:
            # 读取麦克风数据
            data = stream.read(4096)
            # 执行识别
            if recognizer.AcceptWaveform(data):
                # 完整句子识别完成，输出结果
                result = json.loads(recognizer.Result())
                print(f"识别结果：{result['text']}")
            # 可选：实时显示部分结果（取消注释即可）
            # else:
            #     partial = json.loads(recognizer.PartialResult())
            #     print(f"\r识别中：{partial['partial']}", end="", flush=True)
    except KeyboardInterrupt:
        print("\n\n识别已手动停止")
    finally:
        # 安全关闭麦克风与资源
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
