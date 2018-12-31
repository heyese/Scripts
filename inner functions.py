
# Inner functions as closures
import time



def timing_decorator(f):
    def wrapper(x):
        before = time.perf_counter()
        f(x)
        after = time.perf_counter()
        print(f'That took {(after - before):.4f} seconds')
    return wrapper


@timing_decorator
def print_factors(x):
    num_factors = 0
    for i in range(1, x+1):
        if x % i == 0:
            num_factors += 1
    return num_factors


print_factors(5)

print_factors(2424133)