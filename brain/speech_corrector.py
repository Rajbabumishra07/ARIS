class SpeechCorrector:

    def __init__(self):

        self.rules = {

            "come up in chrome": "open chrome",
            "chrome kholo": "open chrome",
            "open crome": "open chrome",
            "open chrom": "open chrome",

            "vs gold": "open vs code",
            "v s gold": "open vs code",
            "vscode": "open vs code",
            "code kholo": "open vs code",

            "goal": "google",
            "gugal": "google",
            "gogle": "google",

            "the music": "play music",
            "music chalao": "play music",

            "youtube kholo": "open youtube",
            "browser kholo": "open browser"
        }

    def correct(self, text):

        text = text.lower().strip()

        if text in self.rules:
            return self.rules[text]

        for wrong, correct in self.rules.items():

            if wrong in text:
                return text.replace(wrong, correct)

        return text


speech_corrector = SpeechCorrector()