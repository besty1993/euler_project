import math

def is_prime(num) :
    if num <= 1 : return False
    for i in range(2, int(math.sqrt(num))+1) :
        if num%i == 0 :
            return False
    return True

def get_prime_factors(num) :
    factors = []
    min_range = 2
    max_range = num
    while max_range != 1 :
        for i in range(min_range, max_range+1) :
            if max_range%i == 0 and is_prime(i) :
                factors.append(i)
                min_range = i
                max_range = int(max_range//i)
                break
    return factors

if __name__ == '__main__' :
    # print(2**4*3**2*5*7*11*13*17*19)
    for i in range(1,21) :
        print(232792560%i==0)