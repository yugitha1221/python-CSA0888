matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
n=len(matrix)
row_sum=[0]*n
col_sum=[0]*n
main_diag=0
sec_diag=0

for i in range(n):
    for j in range(n):
        row_sum[i] += matrix[i][j]
        col_sum[j] += matrix[i][j]
        if i==j:
            main_diag += matrix[i][j]
        if i+j==n-1:
            sec_diag += matrix[i][j]
print(row_sum)
print(col_sum)
print(main_diag)
print(sec_diag)
