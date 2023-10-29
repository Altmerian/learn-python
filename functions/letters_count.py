def upper_lower_count(sentence):
    upper = 0
    lower = 0
    for letter in sentence:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return upper, lower


phrase = input("Enter a sentence: ")
upper_count, lower_count = upper_lower_count(phrase)
print("Upper case count: ", upper_count)
print("Lower case count: ", lower_count)
