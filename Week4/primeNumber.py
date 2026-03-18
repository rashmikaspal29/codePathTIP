def is_prime(n):
    num = 2
    while num <= n-1: # while num < n

        if n % num == 0:
            return False
        num += 1
        
    return True

print(is_prime(2))