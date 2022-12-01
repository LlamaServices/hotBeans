from pandas import DataFrame
from random import randint
'''
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have
to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if we look at the matrix as a series of rectangles,
        # first starting at the outer most edges of the matrix
        # then moving inwords by one element to get to the next rectangle
        # we can seperate the problem into 'cycles',
        # where each cycle is the process of rotating
        # the edges of the rectangle were looking at.

        # for example, if we have a 4x4 matrix, we would
        # have two cycles, where the first is rotating
        # the 16 elements on the outer most edge of the matrix,
        # then the next and final cycle would be the 2x2
        # in the middle

        # with each cycle, instead of packing a side of the rectangle of elements
        # into a list, then packing the next side, then the next, which
        # would basically be just creating a new matrix at that point
        # we instead use 4 variables to store the 4 corners of the rectangle
        # and switch them, then store the next 4 numbers going from left to right
        # and so on, which (i think) would make the memory complexity constant
        # since no matter what size the matrix, we always only store 4 numbers
        # at a time.

        n = len(matrix[0])
        '''
        # determining the number of cycles
        if n % 2 == 0:
            # no middle
            cycles = n // 2
        if n % 2 != 0:
            # has a middle element
            # but that middle doesnt rotate,
            # so the number of cycles is still the same
            # in other terms, (n - 1) / 2
            cycles = (n-1) // 2
        '''
        cycles = n // 2

        #print('cycles= ', cycles)
        #print()
        n -= 1
        for cycle in range(cycles):
            #print(DataFrame(matrix))
            #print('cycle: ', cycle)
            # note for later,
            # some of these pointer move in the exactly the same way
            # which means they can be the same variable
            # thus saving on space

            i1 = cycle
            j1 = cycle

            i2 = cycle
            j2 = n - cycle

            i3 = n - cycle
            j3 = n - cycle

            i4 = n - cycle
            j4 = cycle

            # this is what actually goes through every side of the rectangle
            for c in range(0, n-cycle):
                if n-cycle == 2 and c == 1 and cycles != 1:
                    break

                #print('i1, j1: ', matrix[i1][j1])
                #print('n-cycle: ', n, '-', cycle, '=', n-cycle, sep='')
                
                #matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i2][j2], matrix[i3][j3], matrix[i4][j4], matrix[i1][j4]
                #matrix[i2][j2], matrix[i3][j3], matrix[i4][j4], matrix[i1][j1] = matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4]
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]
                #tmp1 = matrix[i1][j1]
                #tmp2 = matrix[i2][j2]
                #tmp3 = matrix[i3][j3]
                #tmp4 = matrix[i4][j4]
                #matrix[i2][j2] = tmp1
                #matrix[i3][j3] = tmp2
                #matrix[i4][j4] = tmp3
                #matrix[i1][j1] = tmp4


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

#matrix = [[randint(10, 31) for c in range(7)] for i in range(7)]

#print(DataFrame(matrix))
testinstance = Solution()
testinstance.rotate(matrix)
print(DataFrame(matrix))