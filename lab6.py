import numpy as np

n = int(input("n*n "))
min = int(input())   
max = int(input()) 
matrix = np.random.randint(min, max + 1, size=(n, n))
print(matrix)

for i in range(0,n):
    s = 0
    for x in range(0,n):
        if matrix[x][i] > 0:
            s += matrix[x][i]
    matrix[i, i] = s // n
print(matrix)
