class NMTModel:
    def __init__(self):
        self.name = "Rule-Based NMT Model"
        self.dictionary = self._build_dictionary()

        print(f"{self.name} initialized successfully")

    def _build_dictionary(self):
        return {
            "processor": "المعالج",
            "system": "النظام",
            "device": "الجهاز",
            "cooling fan": "مروحة تبريد",
            "connections": "اتصالات",
            "motherboard": "اللوحة الأم",
            "components": "المكونات"
        }

    def translate(self, text):
        words = text.split()
        translated_words = []

        for word in words:
            translated_word = self._translate_word(word)
            translated_words.append(translated_word)

        sentence = " ".join(translated_words)
        return self._postprocess(sentence)

    def _translate_word(self, word):
        word = word.lower()

        if word in self.dictionary:
            return self.dictionary[word]

        return word  # keep original if not found

    def _postprocess(self, sentence):
        return sentence.strip()

    def add_translation(self, word, translation):
        self.dictionary[word.lower()] = translation

    def show_dictionary(self):
        print("\nCurrent Translation Dictionary:")
        for k, v in self.dictionary.items():
            print(f"{k} -> {v}")
