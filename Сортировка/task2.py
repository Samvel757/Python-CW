import re

text = "An apple is on the orange table."
vowel_words = re.findall(r"\b[AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя]\w*", text)
print(vowel_words)
