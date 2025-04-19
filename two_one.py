"""
Task 2.1
    This program contains a function to calculate the sum of the first `n` prime numbers.
    Functions:
        sum_of_primes(n): Calculates the sum of the first `n` prime numbers.
        Args:
            n (int): The number of prime numbers to sum.
        Returns:
            int: The sum of the first `n` prime numbers.
        Algorithm:
            1. Use the Sieve of Eratosthenes to generate a list of prime numbers.
            2. Overestimate the range of numbers to ensure at least `n` primes are found.
            3. Sum the first `n` primes from the generated list.
        Notes:
            - The range for the sieve is overestimated as `15 * n` to ensure enough primes are generated.
            - The algorithm assumes `n` is a positive integer.
            - The function may not be efficient for very large values of `n` due to the overestimation and memory usage.
    """

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









