# HW04 – 大模型文案、声音库与语音识别实践

## 环境要求
- Python 3.8+
- 安装依赖：`pip install openai edge-tts openai-whisper`

## 任务一：大模型生成文稿
- 脚本：`task1_generate_article/generate_article.py`
- 生成的文章见 `generated_article.txt`（≥200字）

## 任务二：文本转音频（TTS）
- 脚本：`task2_tts/text_to_speech.py`（使用 edge-tts）
- 输出音频：`output_speech.mp3`


## 任务三：Whisper 语音识别
- 脚本：`task3_whisper/transcribe_audio.py`
- 识别文本：`transcribed_text.txt`


## 如何运行
```bash
cd hw04
python task1_generate_article/generate_article.py
python task2_tts/text_to_speech.py
python task3_whisper/transcribe_audio.py
