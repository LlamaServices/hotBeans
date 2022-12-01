from pandas import DataFrame

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0])
        cycles = n // 2

        #print('cycles= ', cycles)
        #print()
        n -= 1
        flag = True
        somefuckingcounter = 1
        for cycle in range(cycles):
            #print(DataFrame(matrix))
            #print('cycle: ', cycle)

            i1 = cycle
            j1 = cycle

            i2 = cycle
            j2 = n - cycle

            i3 = n - cycle
            j3 = n - cycle

            i4 = n - cycle
            j4 = cycle

            for c in range(0, n-cycle):
                if n-cycle == 2 and c == 1 and cycles != 1:
                    break
                if somefuckingcounter > 1 and c == n-cycle-1:
                    break

                #print('i1, j1: ', matrix[i1][j1])
                #print('n-cycle: ', n, '-', cycle, '=', n-cycle, sep='')
                
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]


                #print(cycle)
                #print('i1: ', i1, 'j1: ', j1)
                #print('i2: ', i2, 'j2: ', j2)
                #print('i3: ', i3, 'j3: ', j3)
                #print('i4: ', i4, 'j4: ', j4)
                #print()

                # 1'st side
                j1 += 1
                
                # 2'nd side
                i2 += 1
                
                # 3'rd side
                j3 -= 1

                # 4'th side
                i4 -= 1
            somefuckingcounter += 1
            #print()


matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix = [
    [ 1, 2, 3, 4, 5],
    [ 6, 7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

matrix = [
    [ 2,29,20,26,16,28],
    [12,27, 9,25,13,21],
    [32,33,32, 2,28,14],
    [13,14,32,27,22,26],
    [33, 1,20, 7,21, 7],
    [ 4,24, 1, 6,32,34]
]



#matrix = [[randint(10, 31) for c in range(7)] for i in range(7)]

#print(DataFrame(matrix))
testinstance = Solution()
testinstance.rotate(matrix)
print(DataFrame(matrix))