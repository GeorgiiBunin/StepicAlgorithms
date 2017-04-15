def find_sums(m):
    res = []
    i = 0
    sum_els = 0
    while sum_els < m:
        res.append(i)
        sum_els += i
        i += 1
        if sum_els == m:
            del res[0]
            return res
    d = len(res)

    for i in range(d, 0, -1):
        sum_els -= res[-1]
        del res[-1]
        while sum_els < m:
            res[-1] += 1
            sum_els += 1
            if sum_els == m:
                del res[0]
                return res



def main():
    m = int(input())
    n = find_sums(m)
    print(len(n))
    for item in n:
        print(item, end=' ')


if __name__ == "__main__":
    main()
