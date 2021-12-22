# Fibonacci
def fib(n):
    """
    Returns the fibonacci value of n starting from 1
      fib(1) -> 1
    """
    # base case
    if n == 0:
        return 0

    # recursive case
    return n - fib(n-1) 
