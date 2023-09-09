import pyaudio
import wave
import numpy as np

# pyaudio allows to use python to play/record audio
# wave allows to use python to read/write audio (WAV) files

CHUNK = 1024                # Buffer size
FORMAT = pyaudio.paInt16    # Data type
CHANNELS = 2                # Number of channels
RATE = 22050                # Sample rate (Hz)
RECORD_SECONDS = 5          # Duration
WAVE_OUTPUT_FILENAME = "test.wav"

# Get pyaudio object
p = pyaudio.PyAudio()

# Open audio stream (from default device)
stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK) 

# Append frames of data
frames = []
all_left=[]
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # Read raw data and append
    raw_data = stream.read(CHUNK)
    frames.append(raw_data)
    
    # Convert to numpy array
    interleaved_data = np.frombuffer(raw_data, dtype=np.int16)

    # Extract left and right values
    left = interleaved_data[::2] 
    right = interleaved_data[1::2]  

    

    # Report volume (on left)
    print("L: {0:.2f}, R: {1:.2f}".format(np.mean(np.abs(left)), np.mean(np.abs(right))))

    print(interleaved_data)
    #all_left=all_left.append(left)

# Shutdown
stream.stop_stream()
stream.close()
p.terminate()

# LP: txt is a funny format for array data!
# csv is better, althogh a bit heavy (bot are actually just text files).
# a good alternative would be a binary format, like npy or npz
np.savetxt('interleaved_data.txt', interleaved_data)


# Here I want a digital recording of the audio 
# Save a wav file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
