# 裁切聲音
from pydub import AudioSegment

audio = AudioSegment.from_file('input.wav', format='wav')

# 起始結束時間(毫秒)
startTime = 5000
endTime = 25000

clippedAudio = audio[startTime:endTime]

clippedAudio.export('output.wav', format='wav')