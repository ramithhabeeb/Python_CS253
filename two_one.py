

def sum_of_primes(n):
    isprime = [True] * 15*n   # 15*n is an overestimate of the nth prime
    isprime[0] = isprime[1] = False

    for i in range(2, int((15*n)**0.5) + 1):
        if isprime[i]:
            for j in range(i*i, 15*n, i):
                isprime[j] = False
    primes = [i for i in range(2, 15*n) if isprime[i]]
    sum = 0
    for i in range(n):
        sum += primes[i]
    return sum









