matrix = []
for i in range(1, 6):
    sub = []
    for j in range(1, 6):
        sub.append((i, j))
    matrix.append(sub)

print(matrix)
for i in matrix:
    for j in i:
        print(j)
    print("\v")