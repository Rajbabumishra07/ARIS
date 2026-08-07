import os
import json
import queue
import time

import sounddevice as sd
from vosk import Model, KaldiRecognizer

q = queue.Queue()

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "vosk-model-small-en-in-0.4"
)

# ---------------- Lazy Load ---------------- #

_model = None
_recognizer = None


def _init_voice():

    global _model, _recognizer

    if _model is not None:
        return

    total = time.perf_counter()

    print("⚡ Loading Voice Model...")

    t = time.perf_counter()

    _model = Model(MODEL_PATH)

    print(f"📦 Model Loaded : {time.perf_counter()-t:.2f}s")

    t = time.perf_counter()

    _recognizer = KaldiRecognizer(_model, 16000)

    print(f"🎤 Recognizer : {time.perf_counter()-t:.2f}s")

    _recognizer.SetWords(True)
    _recognizer.SetPartialWords(False)

    print(f"✅ Voice Ready ({time.perf_counter()-total:.2f}s)")


def callback(indata, frames, time_info, status):

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

    _init_voice()

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

            if _recognizer.AcceptWaveform(data):

                result = json.loads(_recognizer.Result())

                text = clean_text(
                    result.get("text", "")
                )

                if len(text) < 2:
                    continue

                print("🎧 Heard:", text)

                return text