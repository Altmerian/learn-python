codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---']

text = 'deface'

for char in text:
    print(codes[ord(char) - ord('a')], end=' ')
