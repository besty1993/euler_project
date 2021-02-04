"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time

"""
the 1st square 1x1 : 1
the 2nd square 3x3 : 1^2+2*1, 1^2+2*2, 1^2+2*3, 1^2+2*4
the 3rd square 5x5 : 3^2+4*1, 3^2+4*2, 3^2+4*3, 3^2+4*4
the 4th square 7x7 : 5^2+6*1, 5^2+6*2, 5^2+6*3, 5^2+6*4 ...
"""
def square_edges(side_size) :
    assert side_size > 0
    if side_size == 1 : return [1]
    temp = side_size-2
    return [temp**2 + n*(temp+1) for n in range(1, 5)]

if __name__ == '__main__' :
    stime = time.time()
    
    answer = []
    grid_size = 1001
    for i in range(1,grid_size+1,2) :
        answer.extend(square_edges(i))
    answer = sum(answer)

    print(answer, time.time()-stime)