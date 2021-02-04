# https://projecteuler.net/problem=30
import time

def find_special_nums(powers) :
    nums = []
    for num in range(0, powers*10**powers) :
        digits = [int(n) for n in str(num)]
        fifths = sum([n**powers for n in digits])
        if len(digits) <= 1 : continue
        if num == fifths :
            nums.append(num)
    return nums


if __name__ == '__main__' :
    stime = time.time()
    
    answer = find_special_nums(5)
    answer = sum(answer)

    print(answer, time.time()-stime)