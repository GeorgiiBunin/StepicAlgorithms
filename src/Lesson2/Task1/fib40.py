def fib_array(n):
    """

    :type n: int
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def main():
    n = int(input())
    print(fib_array(n))


if __name__ == "__main__":
    main()
