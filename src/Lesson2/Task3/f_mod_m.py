from builtins import range


def get_pisano_period(m):
    a = 0
    b = 1
    for i in range(0, m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1
    return 0


def fib_mod(n, m):
    r = n % get_pisano_period(m)

    first = 0
    second = 1

    res = r

    for i in range(1, r):
        res = (first + second) % m
        first = second
        second = res
    return res % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
