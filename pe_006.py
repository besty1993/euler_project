def sum_all(num) :
    return int((num+1)*(num)//2)

def sum_squares(num) :
    return sum([i**2 for i in range(num+1)])

if __name__ == '__main__' :
    num = 100
    print(sum_all(num)**2 - sum_squares(num))