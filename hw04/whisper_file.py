import whisper
import time
import os

def transcribe_audio(audio_path, output_txt="result_file.txt"):
    """
    任务三要求1：识别本地音频文件
    :param audio_path: 音频文件路径
    :param output_txt: 输出文本路径
    """
    print("="*50)
    print("任务三：基于Whisper的音频文件识别")
    print("="*50)
    
    # 1. 加载模型 (tiny/base/small/medium/large)
    model = whisper.load_model("base")
    print(f"模型加载完成：base")

    # 2. 检查音频文件
    if not os.path.exists(audio_path):
        print(f"错误：未找到音频文件 {audio_path}，请检查路径。")
        return

    # 3. 执行识别
    start_time = time.time()
    print(f"开始识别音频：{audio_path} ...")
    result = model.transcribe(audio_path, language="zh", verbose=False)
    end_time = time.time()

    # 4. 输出结果
    print("\n【识别结果预览】")
    print(result["text"])
    print(f"\n耗时：{end_time - start_time:.2f} 秒")

    # 5. 保存结果
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"\n识别结果已保存至：{output_txt}")
    return result["text"]

if __name__ == "__main__":
    # 请将导出的音频文件放在此目录下
    AUDIO_FILE = "配音音频.mp3" 
    transcribe_audio(AUDIO_FILE)
