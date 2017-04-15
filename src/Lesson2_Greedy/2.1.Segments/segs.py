def act_sel(x: list) -> list:
    """
    picks maximal amount of non-overlapping segments from a list of segments.
    :param x: list of all segments written as lists; x[i][0]<=x[i][1] 
              (the start of the segment is not greater than the end)
    :return: maximal list of non-overlapping lists
    """
    #check on the input
    if not is_list_of_lists(x):
        return print('incorrect input')
    for item in x:
        assert item[0] <= item[1]

    x.sort(key=lambda x: x[1]) #sort by the ends of segments
    n = len(x)
    res = [x[0]]
    for i in range(1, n):
        if x[i][0] > res[-1][1]:
            res.append(x[i])
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
        segments.append([n,m])
    l_of_segs = act_sel(segments)
    print(segments)
    print(l_of_segs)


# if __name__ == "__main__":
main()
