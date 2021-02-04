"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

import time
import math

def fibo(idx:int) :
    assert idx > 0
    if idx < 3 : return 1
    return fibo(idx-1) + fibo(idx-2)

def fibo_list(length:int, target_digits) :
    assert length > 0
    fibos = [1, 1]
    if length < 3 :
        return fibos[:length]
    for l in range(length-2) :
        next_fibo = fibos[-1]+fibos[-2]
        fibos.append(next_fibo)
        if next_fibo//(10**(target_digits-1)) > 0 :
            break
    return fibos
    

if __name__ == '__main__' :
    stime = time.time()
    
    target_digits = 1000
    answer = fibo_list(100000000000000, target_digits)
    answer = len(answer)

    print(answer, time.time()-stime)