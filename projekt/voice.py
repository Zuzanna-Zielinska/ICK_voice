#!pip3 install vosk
#!pip install pyaudio
# requests

#https://alphacephei.com/vosk/models - modele
#https://drive.google.com/drive/u/1/folders/1PrRAXjdrNtalk6n-y42_t1iZUexcPRwB - link do modeli na dysku po polsku i angielsku

from vosk import Model, KaldiRecognizer
import pyaudio
import requests
    
model = Model(r"vosk-model-small-pl-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

url = "http://localhost:5001"
info = {"racketDirection": 1, "velocity": 1}

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        if text[14:-3] == "start":
            info = {"racketDirection": 1, "velocity": 1}
            print("start")
        elif text[14:-3] == "wolniej":
            info = {"racketDirection": 1, "velocity": 1}
            print("wolniej") #PRĘDKOŚĆ PIŁKI: 1-  wolniej o 10%
        elif text[14:-3] == "szybciej":
            info = {"racketDirection": 1, "velocity": 1}
            print("szybciej")#PRĘDKOŚĆ PIŁKI: 2-  szybciej o 10%
        elif text[14:-3] == "mniejsze":
            info = {"racketDirection": 1, "velocity": 1}
            print("mniejsze") #POLE GRY 1 - zmniejszenie wysokości pola o 10%
        elif text[14:-3] == "większe":
            info = {"racketDirection": 1, "velocity": 1}
            print("większe")  #POLE GRY 2 - zwiększenie wysokości pola o 10%
        elif text[14:-3] == "reset":
            info = {"racketDirection": 1, "velocity": 1}
            print("reset") # TABLICA WYNIKÓW - 1 - reset wyniku
        elif text[14:-3] == "mnożenie":
            info = {"racketDirection": 1, "velocity": 1}
            print("mnożenie") # TABLICA WYNIKÓW - 2 - mnożnik bramek
        elif text[14:-3] == "przenieś":
            info = {"racketDirection": 1, "velocity": 1}
            print("przenieś") # TELEPORTACJA PIŁKI - oczekiwane wartości położenia docelowego
        elif text[14:-3] == ("stop"):
            info = {"racketDirection": 1, "velocity": 1}
            print("stop")
            break;
        else:
            print("Bad instruction")
            print(f"' {text[14:-3]} '")

        # response = requests.post(url, json=info)
        # response.json()

        # print(response.status_code)





# jeśli response = 201, to znaczy, że wszystko się poprawnie wysłało


