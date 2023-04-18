# 2 задача
a = [1, 4, 6]
b = [11, 33, 22]

c = sorted(a, key=lambda x: b[a.index(x)])
print(c)