import glob
import json

class Locale:
    lang = []

    @staticmethod
    def load(lang_dir : str = "./locales/") -> None:
        for locale in glob.glob("*.json", root_dir=lang_dir):
            locale_code = locale.split(".json")[0]
            with open(lang_dir + locale, 'r', encoding='utf-8') as f:
                Locale.lang[locale_code] = json.load(f)

    @staticmethod
    def get(locale_code : str, text : str):
        return Locale.lang[locale_code][text]
