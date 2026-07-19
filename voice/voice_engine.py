import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import os

q = queue.Queue()

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "vosk-model-small-en-us-0.15"
)

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)


def callback(indata, frames, time, status):

    if status:
        print(status)

    q.put(bytes(indata))


def get_command():

    while not q.empty():
        q.get()

    print("\n🎤 Listening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=4000,
        dtype="int16",
        channels=1,
        callback=callback
    ):

        while True:

            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "").lower().strip()

                if len(text) < 2:
                    continue

                print("🎧 Heard:", text)

                return text