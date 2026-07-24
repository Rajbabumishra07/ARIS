import os
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

q = queue.Queue()

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "vosk-model-small-en-in-0.4"
)

model = Model(MODEL_PATH)

recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)

# Ignore very small noises
recognizer.SetPartialWords(False)


def callback(indata, frames, time, status):

    if status:
        return

    q.put(bytes(indata))


def clean_text(text):

    text = text.lower().strip()

    garbage = [
        "uh",
        "um",
        "hmm",
        "erm",
        "ah",
        "the",
    ]

    words = []

    for word in text.split():

        if word in garbage:
            continue

        words.append(word)

    return " ".join(words).strip()


def get_command():

    while not q.empty():
        q.get()

    print("\n🎤 Listening...")

    device = sd.default.device[0]

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        device=device,
        dtype="int16",
        channels=1,
        callback=callback,
    ):

        while True:

            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = clean_text(
                    result.get("text", "")
                )

                if len(text) < 2:
                    continue

                print("🎧 Heard:", text)

                return text