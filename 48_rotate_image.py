from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix = [x.reverse() for x in matrix]

        # temp = matrix[top][left]  # Store the top-left element in a temporary variable
        # matrix[top][left] = matrix[bottom-left]  # Move the bottom-left element to the top-left
        # matrix[bottom-left] = matrix[bottom-right]  # Move the bottom-right element to the bottom-left
        # matrix[bottom-right] = matrix[top-right]  # Move the top-right element to the bottom-right
        # matrix[top-right] = temp  # Finally, place the original top-left (stored in temp) to the top-right

        # n = len(matrix)  # Size of the matrix

        # # Rotate layers from the outermost to the innermost
        # for i in range(n // 2):  # Loop through each layer (from outer to inner)
        #     for j in range(i, n - i - 1):  # Loop through elements in the current layer
        #         # Save the top element in a temporary variable
        #         temp = matrix[i][j]

        #         # Move the left element to the top
        #         matrix[i][j] = matrix[n - j - 1][i]

        #         # Move the bottom element to the left
        #         matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

        #         # Move the right element to the bottom
        #         matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

        #         # Move the top element (stored in temp) to the right
        #         matrix[j][n - i - 1] = temp
