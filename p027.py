import time
from functools import reduce

import numpy as np

from p005 import *

def quad_eq(a, b, n) :
    val = int(n**2 + a*n + b)
    return val

def find_prime_producer(a_range, b_range) :
    prime_producers = []
    num_of_primes = []
    for a in range(a_range*(-1)+1, a_range) :
        for b in range(0, b_range) :
            is_prime_producer=False
            if not is_prime(b) :
                continue
            for n in range(0, 80) :
                eq = quad_eq(a, b, n)
                if eq <= 0 :
                    prime_producers.append([a,b])
                    num_of_primes.append(n)
                    break
                if not is_prime(eq) :
                    prime_producers.append([a,b])
                    num_of_primes.append(n)
                    break
    return prime_producers, num_of_primes


if __name__ == '__main__' :
    stime = time.time()
    
    prime_producers, num_of_primes = find_prime_producer(1000, 1000)
    idx = np.argmax(num_of_primes)
    answer = reduce((lambda x,y:x*y), prime_producers[idx])

    print(answer, time.time()-stime)