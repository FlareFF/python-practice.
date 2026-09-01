matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trace = 0
anti_trace = 0
for i in range(len(matrix)):
    trace += matrix[i][i]
    anti_trace += matrix[i][2 - i]
print(anti_trace)
