food = ['pizza', 'nuggets', 'hotdog', 'noodles',  'pasta', 'burger']

letter = input("Enter a letter: ")

print([x for x in food if x.startswith(letter)])
