import whisper
import time
import os

def main():
    print("===== 任务3.1：Whisper 音频文件识别 =====")
    # 加载模型
    print("正在加载 Whisper  base 模型...")
    model = whisper.load_model("base")

    # 音频路径
    audio_path = "output.mp3"

    if not os.path.exists(audio_path):
        print("错误：请先在本地生成 output.mp3")
        return

    # 开始识别
    print("开始识别音频，请稍候...")
    t1 = time.time()
    result = model.transcribe(audio_path, language="zh")
    t2 = time.time()

    # 输出结果
    print("\n===== 识别结果 =====")
    print(result["text"])
    print(f"\n识别耗时：{t2 - t1:.2f} 秒")

    # 保存到文件
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("结果已保存至 result.txt")

if __name__ == "__main__":
    main()
