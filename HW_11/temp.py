a = [[1, 2, 3], [1, 2, 3]]
b = [[1, 2, 3], [1, 2, 3]]
c = [[2, 1, 3], [2, 1, 3]]
d = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print(a == b)
print(a == c)
print(a == d)
# print([" ".join(map(str, i)) for i in a])
print("\n".join([" ".join(map(str, i)) for i in a]))

a = (1, 2)
b = (1, 2)
c = (2, 1)
d = (3, 4)

print(a == b)
print(a == c)
print(a == d)