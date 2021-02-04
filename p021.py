import math

def get_divisors(num) :
    divisors = []
    for n in range(1, int(math.sqrt(num))+1) :
        if num%n == 0 :
            divisors.extend([n, num//n])
    return sorted(list(set(divisors)))[:-1]

d = lambda n : sum(get_divisors(n))

if __name__ == '__main__' :
    amicables = []
    max_num = 10000
    # max_num = 285
    for i in range(1, max_num) :
        d_temp = d(i)
        if d_temp == i or d_temp >= max_num or i in amicables  : 
            continue
        elif d(d_temp) == i :
            amicables.extend([i, d_temp])
    print(amicables)
    print(sum(amicables))