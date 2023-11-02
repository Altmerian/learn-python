items = [1, 2, [3, 4, [5, [6]], 7], 8, [9, 10]]


def flatten(sequence):
    for item in sequence:
        if hasattr(item, '__iter__'):
            yield from flatten(item)
        else:
            yield item


generator = flatten(items)

for i in generator:
    print(i, end=' ')
