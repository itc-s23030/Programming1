a, a1 = divmod(23, 2)
b, b1 = divmod(11, 2)
c, c1 = divmod(5, 2)
d, d1 = divmod(2, 2)
e, e1 = divmod(1, 2)
print(e1, d1, c1, b1, a1)
b23 = ""
f = 23
while f != 0:
    f, r = divmod(f, 2)
    b23 = str(r) + b23
print(b23)
