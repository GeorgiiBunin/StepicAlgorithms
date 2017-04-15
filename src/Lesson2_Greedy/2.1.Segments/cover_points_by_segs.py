def point_cover(x: list) -> list:
    """

    :param x: a set of n real numbers
    :return: a minimal list of segments of length = 1 that cover all of the points
    """
    x.sort()
    i = 0
    n = len(x)
    res = []
    while i < n:
        seg = [x[i], x[i] + 1]
        res.append(seg)
        i += 1
        while i < n and x[i] <= seg[1]:
            i += 1
    return res


def main():
    a = [float(x) for x in input().split()]
    l_of_segs = point_cover(a)
    print(l_of_segs)


if __name__ == "__main__":
    main()
