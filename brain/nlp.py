class NLP:

    def normalize(self, text):

        text = text.lower().strip()

        replace = {

            "khol do": "open",
            "kholo": "open",
            "chalu karo": "open",
            "start karo": "open",

            "band karo": "close",
            "band kar do": "close",
            "close kar do": "close",

            "chalao": "play",
            "play karo": "play",
            "bajao": "play",
            "laga do": "play",

            "google kholo": "open google",
            "youtube kholo": "open youtube",
            "chrome kholo": "open chrome",

            "hanuman ji": "hanuman chalisa",
            "bajrangbali": "hanuman chalisa",

        }

        for old, new in replace.items():
            text = text.replace(old, new)

        return text


nlp = NLP()