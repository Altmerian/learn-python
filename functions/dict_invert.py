def invert_dict(d):
    return {v: k for k, v in d.items()}


before = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
after = invert_dict(before)
print(after)
