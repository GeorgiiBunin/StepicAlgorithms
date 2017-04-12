def fib_digit(n):
    """

    :type n: int
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % 10)
    return f[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
