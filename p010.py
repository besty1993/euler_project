from p005 import is_prime
limit = 2000000
primes = [n for n in range(3, limit-1, 2) if is_prime(n)]
print(sum(primes)+2)