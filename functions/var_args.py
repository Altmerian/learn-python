def minimum(*args, lower_limit=None):
    if lower_limit is None:
        return min(args)
    else:
        new_list = [x for x in args if x >= lower_limit]
        return min(new_list)


print(minimum(1, 2, 3, 4, -5, 6, 7, 8, 9, 10))
print(minimum(1, 2, 3, 4, -5, 6, 7, 8, 9, 10, lower_limit=6))
