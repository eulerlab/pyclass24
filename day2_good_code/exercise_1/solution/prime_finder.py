from numpy import random

def miller_rabin_prime_test(n, k_iteration = 5):
    """Miller-Rabin primality test"""
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Run k iterations of the Miller-Rabin test
    for i in range(k_iteration):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def fermat_prime_2(n):
    # Choose a random number between 2 and n-1
    if n==2:
        return True
    else:
        a = random.randint(2, n-1) # could be optimized
        
        # Check if a^(n-1) mod n is equal to 1
        if pow(a, n-1, n) == 1:
            return True  # n may be prime
        else:
            return False  # n is definitely composite