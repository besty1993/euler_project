import time
from pe_021 import *

if __name__ == '__main__' :
    stime = time.time()
    
    candidates = set(range(1,28124))
    abundants = [i for i in range(1,28124) if i<sum(get_divisors(i))]
    sum_of_abundants = set([i+j for i in abundants for j in abundants])
    answer = sum(candidates-sum_of_abundants)

    print(answer, time.time()-stime)