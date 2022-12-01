class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0])
        cycles = n // 2
        n -= 1

        for cycle in range(cycles):
            i1 = cycle
            j1 = cycle

            i2 = cycle
            j2 = n - cycle

            i3 = n - cycle
            j3 = n - cycle

            i4 = n - cycle
            j4 = cycle

            while j1 < n-cycle:
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]

                # 1'st side
                j1 += 1
                
                # 2'nd side
                i2 += 1
                
                # 3'rd side
                j3 -= 1

                # 4'th side
                i4 -= 1