import re

def extract_vowel_words(text):
    words = re.findall(r'\b[aeiouAEIOUаеиоуыэюяАЕИОУЫЭЮЯ]\w*', text)
    return words

text = "Аня ела арбуз и огурцы утром"
print(extract_vowel_words(text))