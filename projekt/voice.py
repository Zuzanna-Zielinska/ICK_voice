#!pip3 install vosk
#!pip install pyaudio
#!pip install requests

#https://alphacephei.com/vosk/models - modele
#https://drive.google.com/drive/u/1/folders/1PrRAXjdrNtalk6n-y42_t1iZUexcPRwB - link do modeli na dysku po polsku i angielsku

from vosk import Model, KaldiRecognizer
import pyaudio
import requests

url = "http://localhost:5001"         # adres serwera
info = { "id": 1, "scoreboard": 0, "ballVelocity": 1}       # słownik do wysłania

reset_scoreboard = False   # zmienna do resetu wyniku
velocity = 1              # prędkość piłki
v_lower_limit = 0        # dolny limit prędkości
v_upper_limit = 100     # górny limit prędkości
    
model = Model(r"vosk-model-small-pl-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def send_info(reset_scoreboard: bool, velocity: int):
    """Funkcja wysyłająca informacje do serwera - wyjście interfejsu"""

    info = { "id": 1, "scoreboard": int(reset_scoreboard), "ballVelocity": velocity}

    # response = requests.post(url, json=info)
    # response.json()
    #
    # print(response.status_code)

    print(info)

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()

        if text[14:-3] == "reset":
            print("reset")  # TABLICA WYNIKÓW - 1 - reset wyniku
            reset_scoreboard = True

            send_info(reset_scoreboard, velocity)
            reset_scoreboard = False

        elif text[14:-3] == ("stop"):
            print("stop")

            break;

        elif text[14:-3] == ("szybciej"):
            print("szybciej")
            if velocity < v_upper_limit: #blokada przekroczenia górnego limitu
                velocity += 1

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("wolniej"):
            print("wolniej")
            if velocity > v_lower_limit: #blokada przekroczenia dolnego limitu
                velocity -= 1

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("zero"):
            print("zero")
            velocity = 0

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("jeden"):
            print("jeden")
            velocity = 1

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("dwa"):
            print("dwa")
            velocity = 2

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("trzy"):
            print("trzy")
            velocity = 3

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("cztery"):
            print("cztery")
            velocity = 4

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("pięć"):
            print("pięć")
            velocity = 5

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("sześć"):
            print("sześć")
            velocity = 6

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("siedem"):
            print("siedem")
            velocity = 7

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("osiem"):
            print("osiem")
            velocity = 8

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("dziewięć"):
            print("dziewięć")
            velocity = 9

            send_info(reset_scoreboard, velocity)

        elif text[14:-3] == ("dziesięć"):
            print("dziesięć")
            velocity = 10

            send_info(reset_scoreboard, velocity)

        else:
            print("Bad instruction")
            print(f"' {text[14:-3]} '")



# jeśli response = 201, to znaczy, że wszystko się poprawnie wysłało


