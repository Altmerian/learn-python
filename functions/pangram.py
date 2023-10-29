def pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(sentence.lower_count())
    return letters >= alphabet


example = 'the quick brown fox jumps over the lazy dog'
print(pangram(example))
