matr = [[-1, 3, 4],
        [1, -2, 3],
        [10, 5, 6]]

temp = 0
for i in range(len(matr)):
    count = 0
    for j in range(len(matr[0])):
        if matr[i][j] > 0:
            count += 1
    if count == len(matr[0]):
        temp = i
        break

sum1 = 0
for i in range(len(matr[0])):
    sum1 += matr[temp][i]

print(sum1)
