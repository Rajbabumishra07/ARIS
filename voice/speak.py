"""
ARIS V18 Smart Voice Engine
Author : Raj Babu Mishra
"""

import asyncio
import edge_tts
import pygame
import os
import tempfile
import pyttsx3

import voice.state as state


VOICE = "en-US-AndrewNeural"

# ---------------- Lazy Init ---------------- #

_mixer_ready = False
_offline = None


def _init_audio():

    global _mixer_ready, _offline

    if not _mixer_ready:

        pygame.mixer.init()

        _mixer_ready = True

    if _offline is None:

        _offline = pyttsx3.init()

        _offline.setProperty("rate", 180)


# ---------------- Offline ---------------- #

def offline_speak(text):

    _init_audio()

    _offline.say(str(text))

    _offline.runAndWait()


# ---------------- Main Speak ---------------- #

def speak(text):

    state.SPEAKING = True

    _init_audio()

    text = str(text)

    # Date Converter

    if "-" in text and len(text) == 10:

        try:

            day, month, year = text.split("-")

            months = {

                "01": "January",
                "02": "February",
                "03": "March",
                "04": "April",
                "05": "May",
                "06": "June",
                "07": "July",
                "08": "August",
                "09": "September",
                "10": "October",
                "11": "November",
                "12": "December"

            }

            if month in months:

                text = f"{int(day)} {months[month]} {year}"

        except Exception:

            pass

    fd, filename = tempfile.mkstemp(suffix=".mp3")

    os.close(fd)

    try:

        async def _tts():

            communicate = edge_tts.Communicate(

                text=text,

                voice=VOICE,

                rate="+15%",

                volume="+40%"

            )

            await communicate.save(filename)

        asyncio.run(_tts())

        pygame.mixer.music.load(filename)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():

            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

    except Exception as e:

        print()

        print("⚠ Edge TTS Failed")

        print(e)

        print("🔊 Switching to Offline Voice")

        offline_speak(text)

    finally:

        try:

            os.remove(filename)

        except Exception:

            pass

        state.SPEAKING = False