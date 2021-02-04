import time

def get_combs(a_range, b_range) :
    combs = []
    for i in range(a_range[0], a_range[1]+1) :
        for j in range(b_range[0], b_range[1]+1) :
            combs.append(i**j)
    combs = sorted(list(set(combs)))
    return combs

if __name__ == '__main__' :
    stime = time.time()
    
    answer = len(get_combs([2,100], [2,100]))

    print(answer, time.time()-stime)