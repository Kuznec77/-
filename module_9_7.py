def is_prime(func):
    def wraper(a, b, c):
        sum_ = func(a, b, c)
        if sum_ == 1:
            return sum_
        for i in range(2, sum_):
            if not sum_ % i and sum != 2:
                print('Составное')
                return sum_
        print('Простое')
        return sum_

    return wraper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)