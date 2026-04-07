import whisper

model = whisper.load_model("base")  # 可选 "small", "medium"
result = model.transcribe("../task2_tts/output_speech.mp3", language="en")

print("识别结果：")
print(result["text"])

with open("transcribed_text.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
