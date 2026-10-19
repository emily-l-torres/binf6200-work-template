"""Fibonacci numbers, by a function that calls itself twice."""


def fibonacci(n: int) -> int:
    """
    Give back the nth Fibonacci number: 0, 1, 1, 2, 3, 5, 8, ...

    @param n: which number, counting from 0
    @return: the nth Fibonacci number
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_calls(n: int) -> int:
    """
    Count the calls fibonacci(n) makes, itself included.

    @param n: which number, counting from 0
    @return: how many times fibonacci is called to work out fibonacci(n)
    """
    if n < 2:
        return 1
    return 1 + count_calls(n - 1) + count_calls(n - 2)


def main() -> None:
    """Print a few Fibonacci numbers, and how many calls each one took."""
    for n in (5, 10, 20, 30):
        print(n, fibonacci(n), count_calls(n))


if __name__ == "__main__":
    main()
