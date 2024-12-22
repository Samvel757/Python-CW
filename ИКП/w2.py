from itertools import permutations

def generate_words(sequence):
    length = len(sequence)
    words = set()
    for i in range(1, length + 1):
        words.update([''.join(p) for p in permutations(sequence, i)])
    return sorted(words)
   
sequence = "k98ok"
result = generate_words(sequence)
for word in result:
    print(word)