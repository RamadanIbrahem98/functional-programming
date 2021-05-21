from typing import Generator


def numbers(start: int) -> Generator:
    yield start
    yield from numbers(start+1)

def sieve(numGenerator: int) -> Generator:
    prime = next(numGenerator)
    yield prime
    yield from sieve(number for number in numGenerator if number % prime != 0)

primes = sieve(numbers(2))

# print the first 10 primes
for i in range(10):
    print(next(primes))