# ICK_voice

Repozytorium do interfejsu komend głosowych na przedmiot Interfejsy człowiek-komputer.

### Użyte biblioteki:

- vosk - modele do rozpoznawania mowy
- pyaudio - odbieranie dźwięku
- request - korzystanie z REST API

### Uruchomienie projektu

Skrypt uruchamiający rozpoznawanie komend głosowych to plik voice.py w folderze projekt.

Domyślnie projekt nie wysyła nigdzie informacji, tylko rejestruje komendy, zmienia wartości danych do wysłania oraz oba wypisuje.
Do uruchoienia wysyłania danych należy:

 - w linijce 12 wpisać odpowiedni adres serwera,
 - w linijkach 33 - 36 odkomentować kod wysyłający dane do serwera,
 - w linijkach 53 - 56 zakomentować kod zatrzymujący nasłuchiwanie komend za pomocą słowa "stop". Polecenie jest potrzebne do testów i będzie negatywnie wypływało na doświadczenie sterwoania grą, jeśli trafi do gotowej aplikacji.
