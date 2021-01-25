def triangle_number_generator(idx) :
    return idx*(idx+1)/2

def get_divisors(num) :
    divisors = [1, num]
    min_range = 2
    max_range = int(num/2)
    while min_range < max_range :
        for i in range(min_range, max_range) :
            if num//i - num/i == 0. :
                divisors.extend([i, int(num/i)])
                min_range = i+1
                max_range = int(num/(i+1))
                break
            if max_range/min_range != max_range//min_range :
                divisors.extend([min_range, max_range])
                break
    divisors.sort()
    return divisors


if __name__ == '__main__' :
    # print(triangle_number_generator(7))
    print(get_divisors(15))
    # for i in range(7) :
        