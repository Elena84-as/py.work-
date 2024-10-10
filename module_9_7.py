import math


def is_prime(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        res = func(*args, **kwargs)
        for i in range(2, int(math.sqrt(res)) + 1):
            if res % i == 0:
                print('Составное')
            else:
                print('Простое')
                return res
    return wrapper


@is_prime
def sum_three(*args):
    return int(sum(args))


result = sum_three(2, 3, 6)
print(result)
