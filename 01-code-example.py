#
# Type a few code hints and choose Shift-command-L to get help from the Code Llama!
#
def fibonacci(n:int) -> int:
    """
    This function returns the nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci numbers are only defined for non-negative integers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    print(fibonacci(10))

if __name__ == "__main__":
    main()
