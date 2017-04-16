def segs_cover(x: list) -> list:
    """
    :param x: a list of segments
    :return: minimal set of points that belong to all of the segments
    """
    if not is_list_of_lists(x):
        return print('incorrect input')
    for item in x:
        assert item[0] <= item[1]

    x.sort(key=lambda x: x[1])  # sort by the ends of segments
    n = len(x)
    res = [x[0][1]]
    for item in x:
        if res[-1] >= item[0] and res[-1] <= item[1]:
            continue
        else:
            res.append(item[1])
    return res


def is_list_of_lists(x: list, n: int = 2):
    """

    :param x: list of objects
    :param n: non-negative integer
    :return: true if list is a list that consists of lists size n;
             empty list is considered a list of lists for any size n (only empty).
    """
    assert n >= 0
    for item in x:
        if not (isinstance(item, list) and len(item) == n):
            return False
    return True


def main():
    print('enter number of segments: ')

    nsegs = int(input())
    segments = []
    print('enter the start and the end of the segment: ')
    for i in range(nsegs):
        n, m = map(int, input().split())
        segments.append([n, m])
    l_of_segs = segs_cover(segments)
    print(len(l_of_segs))
    for item in l_of_segs:
        print(item, end=' ')


if __name__ == "__main__":
    main()
