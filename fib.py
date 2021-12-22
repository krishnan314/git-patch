# Fibonacci iterative
def fib(n):
    """
    Returns the fibonacci value of n starting from 0
      fib(1) -> 0
    """
    if n == 1: return 0
    if n == 2: return 1
    i, j = 0, 1
    for k in range(3, n + 1):
        i = j
        j = j + k
    return j 
