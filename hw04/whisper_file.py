import whisper
import time
import os

def main():
    """
    任务3：基于Whisper的音频文件语音识别
    功能：读取本地配音音频，完成语音转写，保存结果
    """
    print("=" * 60)
    print("任务3：Whisper 音频文件语音识别")
    print("=" * 60)

    # -------------------------- 1. 配置参数 --------------------------
    # 选择Whisper模型：tiny/base/small/medium/large，笔记本推荐base（平衡速度与精度）
    model_name = "base"
    # 音频文件路径（剪映导出的配音音频，需放在hw04目录下）
    audio_path = "配音音频.mp3"
    # 识别结果保存路径
    output_txt = "result_file.txt"

    # -------------------------- 2. 加载模型 --------------------------
    print(f"正在加载Whisper {model_name} 模型...")
    model = whisper.load_model(model_name)
    print("模型加载完成！")

    # -------------------------- 3. 检查音频文件 --------------------------
    if not os.path.exists(audio_path):
        print(f"错误：未找到音频文件 {audio_path}")
        print("请将剪映导出的配音音频放在hw04目录下，命名为「配音音频.mp3」后重试")
        return

    # -------------------------- 4. 执行语音识别 --------------------------
    print(f"开始识别音频：{audio_path}，请稍候...")
    start_time = time.time()
    # 执行识别，指定语言为中文，关闭verbose以简化输出
    result = model.transcribe(audio_path, language="zh", verbose=False)
    end_time = time.time()

    # -------------------------- 5. 输出与保存结果 --------------------------
    print("\n" + "=" * 60)
    print("【识别结果预览】")
    print(result["text"])
    print("=" * 60)
    print(f"识别耗时：{end_time - start_time:.2f} 秒")
    print(f"音频时长：{result['segments'][-1]['end']:.2f} 秒")
    print(f"实时率：{(end_time - start_time) / result['segments'][-1]['end']:.2f}x")

    # 保存完整识别结果到文件
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"\n识别结果已完整保存至：{output_txt}")

if __name__ == "__main__":
    main()
