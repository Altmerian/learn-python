fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles',  'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta',  'nuggets', 'pizza']

# find the min sum of indices for corresponding food in fav1 and fav2
# for example, pizza is at index 0 in fav1 and at index 5 in fav2
# so the sum of indices for pizza is 5

index1 = len(fav1)
index2 = len(fav2)
favourite_food = None

for i1 in range(index1):
    i2 = fav2.index(fav1[i1])
    if i1 + i2 < index1 + index2:
        index1 = i1
        index2 = i2
        favourite_food = fav1[i1]

print(favourite_food, index1 + index2)
