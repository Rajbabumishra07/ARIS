import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

q = queue.Queue()

# model folder ka path
model = Model("model")

recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)


def callback(indata, frames, time, status):
    if status:
        print(status)

    q.put(bytes(indata))


def listen():

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):

        while True:

            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "")

                text = text.lower().strip()

                # Hinglish Normalization
                replacements = {
                    "he aris": "hey aris",
                    "hey iris": "hey aris",
                    "arris": "aris",
                    "airis": "aris",
                    "chrome kholo": "open chrome",
                    "google kholo": "open google",
                    "youtube kholo": "open youtube",
                    "calculator kholo": "calculator",
                    "notepad kholo": "notepad",
                    "time batao": "time",
                    "samay batao": "time",
                    "date batao": "date",
                    "aaj ki date": "date",
                    "india ke bare me batao": "wiki india",
                    "python ke bare me batao": "wiki python",
                }

                if text in replacements:
                    text = replacements[text]

                if text:
                    print("🎤 Heard:", text)
                    return text