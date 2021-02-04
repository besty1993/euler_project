import math

def get_total_grid_route(grid_size:int) :
    """
    1   1
    1   2   1
    1   3   3   1
    1   4   6   4   1 
    1   5   10  10  5   1
    1   6   15  20  15  6   1...
    The total route of 2x2 grid is the middle number of 5x5 grid(6)
    And it is equal to the middle coefficient of (x+y)^4, which is 4C2
    the total route of 3x3 grid is the middle number of 7x7 grid(20)
    And it is equal to the middle coefficient of (x+y)^6, which is 6C3
    """
    assert grid_size > 0
    return math.factorial(grid_size*2)//(math.factorial(grid_size))**2

if __name__ == '__main__' :
    print(get_total_grid_route(20))
