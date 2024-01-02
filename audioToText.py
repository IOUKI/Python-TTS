# 音檔轉中文

import speech_recognition
r = speech_recognition.Recognizer()

with speech_recognition.AudioFile("output.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio, language='zh-tw')
print(text)