import asyncio
import edge_tts
import os
import time

import voice.state as state

VOICE = "en-US-AndrewNeural"


def speak(text):

    state.SPEAKING = True

    text = str(text)

    # Date ko naturally bolne ke liye
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
                "12": "December",
            }

            if month in months:
                text = f"{int(day)} {months[month]} {year}"

        except Exception:
            pass

    filename = f"voice_{int(time.time() * 1000)}.mp3"

    async def _tts():

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate="+15%",
            volume="+40%"
        )

        await communicate.save(filename)

    asyncio.run(_tts())

    os.startfile(filename)

    # ARIS apni hi awaaz dobara na sune
    time.sleep(2)

    state.SPEAKING = False