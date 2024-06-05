matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose=[[matrix[j][i] for j in range(0,len(matrix[i]))] for i in range(0,len(matrix))]
print(transpose)