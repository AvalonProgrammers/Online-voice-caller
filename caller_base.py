import sounddevice as sd
import numpy as np

# Settings
framerates = [8000, 16000, 24000, 32000, 40000, 48000]
framesetting = 6
framerate = framerates[framesetting-1]

seconds = 2
echo_treshhold = 0.1
channels = 1
# End settings

data = np.zeros(shape=(framerate*seconds, channels))
lastdata = np.zeros(shape=(framerate*seconds, channels))
playable = np.zeros(shape=(framerate*seconds, channels))

def makePlayable():
    global data, lastdata, playable
    for idx, value in enumerate(data):
        if lastdata[idx][0]-data[idx][0] >= echo_treshhold:
            playable[idx][0] = 0.0
        else:
            playable[idx] = data[idx]

print("Recording")

while True:
    temp = data.copy()
    makePlayable()
    data = sd.playrec(data*4, framerate, blocking=True, channels=channels)
    lastdata = data.copy()
