import re

text = "word1,word2;word3|word4.word5"
parts = re.split(r"[,;|.]", text)
print(parts)
