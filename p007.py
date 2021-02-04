from pe_005 import is_prime

if __name__ == '__main__' :
    prime_left = 10000
    # prime_left = 5
    current_prime = 2
    num = 3
    while 1 :
        if is_prime(num) :
            current_prime = num
            prime_left -= 1
        if prime_left == 0 :
            break
        num += 2
    print(num)