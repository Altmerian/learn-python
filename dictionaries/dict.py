dic = {1: "a", "b": 2, 3: "c"}

print(dic)

dic["d"] = 4

print(dic)

dic_k = dic.keys()
print(dic_k)

type(dic_k)

dic_iter = dict((x, x * 2) for x in range(10))

print(dic_iter)

help(dic.fromkeys)

dic_fromkeys = dict.fromkeys([1, 2, 3], "a")

print(dic_fromkeys)
