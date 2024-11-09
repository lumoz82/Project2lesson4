numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range (len(numbers)):
    is_prime = True
    if numbers[i] == 1:
        continue
    elif numbers[i] == 2:
        primes.append(numbers[i])
        continue
    else:
        for j in range(2,numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
        if is_prime == True:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print (primes)
print (not_primes)
