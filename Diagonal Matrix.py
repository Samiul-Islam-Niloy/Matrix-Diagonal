def diagonalMats(mat, n):
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                principal = principal + mat[i][j]
            if (i + j) == (n - 1) and i != j:
                secondary = secondary + mat[i][j]
    sum = principal + secondary
    print(sum)


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
diagonalMats(mat, 3)
