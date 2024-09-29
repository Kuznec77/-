numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
primes = []# список простых чисел
not_primes = [] # список составных чисел
i = 0
for i in range(len(numbers)):
    is_primes = True
    n = numbers[i]
    if n < 2:
        print(n, '- не простое число и не составное число')
        continue
    else:
        k = 2
        j = 0
    while n >= k * k and j != 1:
        if n % k == 0:
            j = 1
            is_primes = False
            break
        k = k + 1
    if not(is_primes):
        not_primes.append(n)
    else:
        primes.append(n)
is_primes = True
print('Простые числа', primes)
print('Составные числа', not_primes)