from googletrans import Translator
import googletrans as gts

trans = Translator()
lang_map = {v: k for k, v in gts.LANGCODES.items()}


class Translate:
    """
    A class for translating text using the Google Translate API.

    Attributes:
    - user_input (str): The text to be translated.
    - to_lang (str): The target language for translation.
    """

    def __init__(self, user_input, to_lang):
        """
        Initializes a Translate object.

        Parameters:
        - user_input (str): The text to be translated.
        - to_lang (str): The target language for translation.
        """
        self.user_input = user_input
        self.to_lang = to_lang

    def validate_lang(self):
        """
        Validates the target language for translation.

        If the target language is a valid language code or language name, it is set as the to_lang attribute.
        Otherwise, a ValueError is raised.

        Returns:
        - str: The validated target language.
        """
        if (
            len(self.to_lang) == 2 and self.to_lang in lang_map.keys()
        ):  # that is, language code
            self.to_lang = self.to_lang
        elif (
            len(self.to_lang) > 2 and self.to_lang in lang_map.values()
        ):  # that is, full language words
            self.to_lang = gts.LANGCODES.get(
                self.to_lang, "This is not a valid language, check look up"
            )
        else:
            raise ValueError(
                "This is not a valid language or language code, check the printed lookup above"
            )

        return self.to_lang

    @property
    def get_lang(self):
        """
        Detects the language of the input text.

        Returns:
        - str: The detected language code.
        """
        self.detected_lang = trans.detect(self.user_input).lang
        return self.detected_lang

    @property
    def translate_input(self):
        """
        Translates the input text to the target language.

        Returns:
        - str: The translated text.
        """
        dest_language = self.validate_lang()
        trans_text = trans.translate(
            text=self.user_input, dest=dest_language, src=self.detected_lang
        )
        return trans_text.text


if __name__ == "__main__":
    text = input("Enter the text you want to translate: ")
    print(f"\nLanguage codes look up: {lang_map}\n")
    lang_of_choice = input(
        "To what language do you want to make the translation? It can be any of the above codes stated: "
    )

    translated = Translate(text, lang_of_choice)

    source_lang = lang_map.get(translated.get_lang)
    dest_lang = (
        lang_map.get(lang_of_choice) if len(lang_of_choice) < 2 else lang_of_choice
    )

    print(
        f"\n\n'{text}' has been translated from {source_lang} to {dest_lang} as \n {translated.translate_input}"
    )
