"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    mtrx = ""
    indx = 0
    while indx < 4:
        for i in matrix:
            mtrx += (" " + str(i[indx]))
        mtrx += "\n"
        indx += 1;
    print(mtrx[0:-1])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(4):
        for j in range(len(matrix)):
            if i == j:
                matrix[j][i] = 1;
            else:
                matrix[j][i] = 0;
#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for i in range(len(m2)):
        col_cpy = [e for e in m2[i]]
        for j in range(4):
            v = 0
            for k in range(4):
                v += m1[k][j] * col_cpy[k]
                m2[i][j] = v


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
