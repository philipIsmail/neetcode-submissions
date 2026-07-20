class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        #reverse
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #transpose
        for row in matrix:
            row.reverse()

        # rows = len(matrix)
        # cols = len(matrix[0])

        # col = -1
        # for i in range(rows):
        #     row_lim = len(matrix) - 1 
        #     col += 1
        #     for j in range(cols):
        #         matrix[i][j] = matrix[row_lim][col]
        #         row_lim -= 1