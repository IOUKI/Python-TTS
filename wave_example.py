# Audio file formats
# .map3 => 有損壓縮格式
# .flac => 無損壓縮格式
# .wav => 未壓縮格式(音頻質量最好，但文件大小也最大)
import wave

# Audio signal parameters
# - number of channels: 通道數量(單聲道 or 雙聲道)
# - sample width: 每個樣本的字節數
# - framerate/sample_rate: 採樣率/採樣頻率
# - number of frames: 幀總數
# - values of a frame: 每一幀的數值

obj = wave.open('test.wav', 'rb')

print(f"number of channels: {obj.getnchannels()}")
print(f"sample width: {obj.getsampwidth()}")
print(f"frame rate: {obj.getframerate()}")
print(f"number of frames: {obj.getnframes()}")
print(f"parameters: {obj.getparams()}")

# 取得時間和秒數
timeAudio = obj.getnframes() / obj.getframerate()
print(timeAudio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

# 創建新的wav
newObj = wave.open('new_test.wav', 'wb')
newObj.setnchannels(1)
newObj.setsampwidth(2)
newObj.setframerate(16000.0)

newObj.writeframes(frames)

newObj.close()