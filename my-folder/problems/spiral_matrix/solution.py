class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        rowStart, rowEnd, colStart, colEnd = 0, m-1, 0, n-1
        ans = []
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                ans.append(matrix[rowStart][i])
            rowStart += 1
            if rowStart > rowEnd or colStart > colEnd:
                break
            for i in range(rowStart, rowEnd + 1):
                ans.append(matrix[i][colEnd])
            colEnd -= 1
            if rowStart > rowEnd or colStart > colEnd:
                break
            for i in range(colEnd, colStart - 1, -1):
                ans.append(matrix[rowEnd][i])
            rowEnd -= 1
            if rowStart > rowEnd or colStart > colEnd:
                break
            for i in range(rowEnd, rowStart - 1, -1):
                ans.append(matrix[i][colStart])
            colStart += 1
            if rowStart > rowEnd or colStart > colEnd:
                break
        return ans
        