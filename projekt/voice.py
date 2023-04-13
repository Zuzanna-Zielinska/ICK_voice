#!pip3 install vosk
#!pip install pyaudio
#https://alphacephei.com/vosk/models - modele
#https://drive.google.com/drive/u/1/folders/1PrRAXjdrNtalk6n-y42_t1iZUexcPRwB - link do modeli na dysku po polsku i angielsku

from vosk import Model, KaldiRecognizer
import pyaudio
    
model = Model(r"C:\\Users\\kstal\\Downloads\\vosk-model-small-pl-0.22")
recognizer = KaldiRecognizer(model, 16000)
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    
while True:
    data = stream.read(4096)
        
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        if text[14:-3] == "start":
            print("start")
        elif text[14:-3] == "wolniej":
            print("wolniej") #PRĘDKOŚĆ PIŁKI: 1-  wolniej o 10%
        elif text[14:-3] == "szybciej":
            print("szybciej")#PRĘDKOŚĆ PIŁKI: 2-  szybciej o 10%
        elif text[14:-3] == "mniejsze":
            print("mniejsze") #POLE GRY 1 - zmniejszenie wysokości pola o 10%    
        elif text[14:-3] == "większe":
            print("większe")  #POLE GRY 2 - zwiększenie wysokości pola o 10%
        elif text[14:-3] == "reset":
            print("reset") # TABLICA WYNIKÓW - 1 - reset wyniku
        elif text[14:-3] == "mnożenie":
            print("mnożenie") # TABLICA WYNIKÓW - 2 - mnożnik bramek 
        elif text[14:-3] == "przenieś":
            print("przenieś") # TELEPORTACJA PIŁKI - oczekiwane wartości położenia docelowego 
        elif text[14:-3] == ("stop"):
            print("stop")
            break;
        else:
            print("Bad instruction")
            print(f"' {text[14:-3]} '")
