from pandas import DataFrame
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
        n = len(matrix[0])

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

        # determining the number of cycles
        if n % 2 == 0:
            # no middle
            cycles = n/2
        if n % 2 != 0:
            # has a middle element
            # but that middle doesnt rotate,
            # so the number of cycles is still the same
            # in other terms, (n - 1) / 2
            cycles = (n-1) / 2

        

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(DataFrame(matrix))