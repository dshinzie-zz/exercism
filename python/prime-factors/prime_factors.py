def prime_factors(number):
    factors = []
    divisor = 2
    while number >= divisor:
        while number % divisor is 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors
