from math import factorial

sum_of_digits = lambda num : sum([int(n) for n in list(str(num))])

if __name__ == '__main__' :
    fac = factorial(100)
    print(sum_of_digits(fac))