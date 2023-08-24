# AとBの演算作成した場合
A = {x for x in range(21)}
print(A)
B = {x for x in range(21) if x % 2 == 0}
print(B)
C = A - B
print(C)

# まとめてやる方法
C = {x for x in range(21) if x % 2 != 0}
print(C)
