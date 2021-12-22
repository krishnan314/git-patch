# Fibonacci
def fib(n):
    """
    Returns the fibonacci value of n starting from 0
      fib(1) -> 0
    """
    # base case
    if n == 1:
        return 0

    # recursive case
    return n + fib(n-1) 
