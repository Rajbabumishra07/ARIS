from translate import Translator

def translate_text(text, language):

    try:
        translator = Translator(to_lang=language)
        return translator.translate(text)

    except Exception:

        return "Translation failed."