def matrix_sums(matrix):
    # Ensure the matrix is square
    n = len(matrix)
    assert all(len(row) == n for row in matrix), "Matrix must be square"

    # Sum of rows
    row_sums = [sum(row) for row in matrix]

    # Sum of columns
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]

    # Sum of main diagonal
    main_diag_sum = sum(matrix[i][i] for i in range(n))

    # Sum of secondary diagonal
    secondary_diag_sum = sum(matrix[i][n-i-1] for i in range(n))

    return row_sums, col_sums, main_diag_sum, secondary_diag_sum

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums, col_sums, main_diag_sum, secondary_diag_sum = matrix_sums(matrix)

print("Row Sums:", row_sums)
print("Column Sums:", col_sums)
print("Main Diagonal Sum:", main_diag_sum)
print("Secondary Diagonal Sum:", secondary_diag_sum)
