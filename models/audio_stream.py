# from transformers import WhisperProcessor, WhisperForConditionalGeneration
import pyaudio
import wave
import assemblyai as aai
import warnings; warnings.filterwarnings("ignore")

# model = whisper.load_model("base")
aai.settings.api_key = "f68b85aa1e3e44d7b9858b12fa688651"
transcriber = aai.Transcriber()
p = pyaudio.PyAudio()

while True:
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    print("Start recording for 5 seconds")
    frames = []
    for i in range(0, int(44100/1024 * 5)): # rate/chunk * secs
        data = stream.read(1024)
        frames.append(data)
    # print("5 secs batch recorded")
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
    
    
    with wave.open("output.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(frames))
        print("Succesfully saved batch")
    text = transcriber.transcribe("output.wav").text
    # text = model.transcribe("output.wav")["text"]
    print(text)
