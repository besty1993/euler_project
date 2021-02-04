import time
import math

def get_lexicographic_permutation(digits:list, idx:int) :
    """
    idx//9! -> 1st number
    idx%9!//8! -> 2nd number
    idx%9!%8!//7! -> 3rd number
    ...
    """
    digits.sort()
    lex = []
    
    left_digits = digits.copy()
    temp_idx = idx-1
    print(len(left_digits)-1)
    for i in range(len(left_digits)-1, 0, -1) :
        fac = math.factorial(i)
        digit_idx = temp_idx//fac
        print(temp_idx, fac, digit_idx)
        digit = left_digits.pop(digit_idx)
        lex.append(digit)
        temp_idx = temp_idx%fac
    lex.append(left_digits[0])
    return lex

if __name__ == '__main__' :
    stime = time.time()
    
    digits = [0,1,2,3,4,5,6,7,8,9]
    lex_idx = 1000000
    answer = get_lexicographic_permutation(digits, lex_idx)

    print(answer, time.time()-stime)