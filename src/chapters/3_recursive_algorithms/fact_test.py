import time

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    n = int(input("Enter a non-negative integer: "))

    print(f"\nCalculating factorial of {n}:")

    start = time.time()
    fact_rec = factorial_recursive(n)
    duration = time.time() - start
    print(f"Recursive factorial: {fact_rec} (Time: {duration:.6f} seconds)")

    start = time.time()
    fact_iter = factorial_iterative(n)
    duration = time.time() - start
    print(f"Iterative factorial: {fact_iter} (Time: {duration:.6f} seconds)")

if __name__ == "__main__":
    main()
