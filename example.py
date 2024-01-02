import speech_recognition
import pyaudio
import wave

def playVoice(audioFileName: str):
    CHUNK = 1024

    # 開啟音檔
    file = wave.open(audioFileName, 'rb')
    # 導入PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(file.getsampwidth()),
        channels=file.getnchannels(),
        rate=file.getframerate(),
        output=True
    )
    # 讀取音源檔
    data = file.readframes(CHUNK)
    # 播放音源檔
    while data:
        stream.write(data)
        data = file.readframes(CHUNK)
    # 停止播放
    stream.stop_stream()
    stream.close()
    # 關閉 PyAudio
    p.terminate()

# 從音源檔轉換文字
def audioFileToText(audioFileName: str):
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audioFileName) as source:
        r.adjust_for_ambient_noise(source, duration=0)
        audio = r.record(source)
        # text = r.recognize_google(audio, language='en-US') # 英文
        text = r.recognize_google(audio, language='zh-tw') # 中文
        return text

# 從麥克風輸入轉換成文字
def voiceToText():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('請開始說話...')
        # 函數調整麥克風噪音
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='zh-TW') # 中文
    except Exception as e:
        text = f'無法翻譯 Error: {e}'
    
    return text

def main():
    outFile = './Voice.txt'
    f = open(outFile, 'w', encoding='utf-8-sig')

    print('播放音檔:')
    audioFileName = 'output.wav'
    playVoice(audioFileName)

    print('轉換語音檔成文字:')
    text = audioFileToText(audioFileName)
    print(text)

    print('口語翻譯成文字:')
    text = voiceToText()
    print(text)

    f.write(text + '\n')
    print(f'\n\n檔案{outFile}已存檔')
    f.close()

if __name__ == '__main__':
    main()