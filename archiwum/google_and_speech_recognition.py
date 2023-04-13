#libraries:
#  - speech_recognition
#  - pyaudio
#  - google-cloud-speech

import speech_recognition as sr
import time

start_time = time.time()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

end_time = time.time()
print("Czas nasłuchu: " + str(end_time - start_time))

speech = ""

# recognize speech using Google Speech Recognition
#engilsh only
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    speech = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said: " + speech)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# speech = "hello hello"

words = speech.split()
print(words)

for word in words:
    if word == "hello":
        print("Hello")
    elif word == "slower":
        print("Slower")
    elif word == "faster":
        print("Faster")
    elif word == "low":
        print("Low")
    elif word == "high":
        print("High")
    elif word == "reset":
        print("Reset")
    elif word == "multiply":
        print("Multiply")
    elif word == "teleport":
        print("Teleport")